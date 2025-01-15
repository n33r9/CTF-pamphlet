# https://github.com/defund/coppersmith/blob/master/README.md

import itertools
from Crypto.Util.number import long_to_bytes

enc = 4782207738169357679017263311695366580149461241803922088835452812820137537830281562950634059939171784035642202164746425519370563906663225547286363495366866588141853586109553019469599011984795232666657032457349167541183811442599555965876853759790930565452169138123206051344200109808603093521161556603615660329142949615063443855551027286822234646698015310643407246009689006200152818931447476595216569044114220319818061396623338764899012025923470408152189436065437542065068815744124506169026323905222443334212867601172364249248963768649488580249031694113977946046461290930755706144535271632419505875554486279354334709794323960679
n = 3964970058588757148381961704143056706462468814335020245520977895524549102412775370911197710398920529632256746343939593559572847418983212937475829291172342816906345995624544182017120655442222795822907477729458438770162855927353619566468727681852742079784144920419652981178832687838498834941068480219482245959017445310420267641793085925693920024598052216950355088176712030006651946591651283046071005648582501424036467542988971212512830176367114664519888193885765301505532337644978456428464159474089450883733342365659030987687637355512103402573155030916404165387863932234088255017821889649456947853403395704387479968208359004918561
ee = [167323, 194700, 130745, 7156, 65616, 200175, 106106, 4410, 94204, 121719, 176084, 168449, 206162, 19151, 165232, 149276, 151372, 64105, 162906, 92391, 69021, 200382, 22272, 14195, 200195, 70505, 46059, 194712, 177080, 209749, 112239, 9882, 23285, 45783, 117745, 31663, 51641, 148822, 169539, 142669]
ff = [300710, 494582, 107979, 208491, 285026, 638043, 525064, 566864, 36622, 212388, 374138, 220683, 193612, 532230, 75887, 548412, 650282, 195040, 74550, 158762, 797511, 322315, 821880, 484339, 76864, 64394, 101586, 815915, 762307, 410750, 115213, 726390, 378350, 800132, 379035, 797320, 413506, 284265, 537835, 226489]
A = 43787291635671214792919526096167649451
C = 156497500579206068939331641182566791023
M = 273364800599018888270443304662600024273


def attack(y, k, s, m, a, c):
    """
    Recovers the states associated with the outputs from a truncated linear congruential generator.
    More information: Frieze, A. et al., "Reconstructing Truncated Integer Variables Satisfying Linear Congruences"
    :param y: the sequential output values obtained from the truncated LCG (the states truncated to s most significant bits)
    :param k: the bit length of the states
    :param s: the bit length of the outputs
    :param m: the modulus of the LCG
    :param a: the multiplier of the LCG
    :param c: the increment of the LCG
    :return: a list containing the states associated with the provided outputs
    """
    diff_bit_length = k - s

    # Preparing for the lattice reduction.
    delta = c % m
    y = vector(ZZ, y)
    for i in range(len(y)):
        # Shift output value to the MSBs and remove the increment.
        y[i] = (y[i] << diff_bit_length) - delta
        delta = (a * delta + c) % m

    # This lattice only works for increment = 0.
    B = matrix(ZZ, len(y), len(y))
    B[0, 0] = m
    for i in range(1, len(y)):
        B[i, 0] = a ** i
        B[i, i] = -1

    B = B.LLL()

    # Finding the target value to solve the equation for the states.
    b = B * y
    for i in range(len(b)):
        b[i] = round(QQ(b[i]) / m) * m - b[i]

    # Recovering the states
    delta = c % m
    x = list(B.solve_right(b))
    for i, state in enumerate(x):
        # Adding the MSBs and the increment back again.
        x[i] = int(y[i] + state + delta)
        delta = (a * delta + c) % m

    return x

a = (attack(ee, 128, 18, M, A, C)[-1] * A + C) % M >> (128 - 18)
b = (attack(ff, 128, 20, M, A, C)[-1] * A + C) % M >> (128 - 20)
print(a, b)

def small_roots(f, bounds, m=1, d=None):
    if not d:
        d = f.degree()

    if isinstance(f, Polynomial):
        x, = polygens(f.base_ring(), f.variable_name(), 1)
        f = f(x)

    R = f.base_ring()
    N = R.cardinality()

    f /= f.coefficients().pop(0)
    f = f.change_ring(ZZ)

    G = Sequence([], f.parent())
    for i in range(m+1):
        base = N^(m-i) * f^i
        for shifts in itertools.product(range(d), repeat=f.nvariables()):
            g = base * prod(map(power, f.variables(), shifts))
            G.append(g)

    B, monomials = G.coefficient_matrix()
    monomials = vector(monomials)

    factors = [monomial(*bounds) for monomial in monomials]
    for i, factor in enumerate(factors):
        B.rescale_col(i, factor)

    B = B.dense_matrix().LLL()

    B = B.change_ring(QQ)
    for i, factor in enumerate(factors):
        B.rescale_col(i, 1/factor)

    H = Sequence([], f.parent().change_ring(QQ))
    for h in filter(None, B*monomials):
        H.append(h)
        I = H.ideal()
        if I.dimension() == -1:
            H.pop()
        elif I.dimension() == 0:
            roots = []
            for root in I.variety(ring=ZZ):
                root = tuple(R(root[var]) for var in f.variables())
                roots.append(root)
            return roots

    return []

pbar=int(sqrt((n*a)//b))
lbits=500
p = 0
while True:
    ln = 2^lbits
    p_length=1042
    q_length=1044
    p_high=pbar//ln

    p0=p_high

    # Recovery starts here
    q0 = floor(n / (p0*ln))//ln
    print("q0 bit lengths: ", len(bin(q0))-2)
    X = Y = 2^(lbits+2) # bounds on x0 and y0


    bounds = (X,Y)
    R = Integers(n)
    PR.<x, y> = PolynomialRing(Zmod(n))

    f = (x+p0*ln)*(y+q0*ln)

    r = small_roots(f, bounds)
    if r == []:
        lbits = lbits + 1
        continue
    print(small_roots(f, bounds))

    print("p = ", p0*ln+r[0][0])
    p = int(p0*ln+r[0][0])
    break

q = n // p
d = pow(0x10001, -1, (p-1)*(q-1))
print(long_to_bytes(pow(enc, d, n)))