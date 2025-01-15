# Giới thiệu về OSINT trong CTF

## 1. OSINT là gì?
**OSINT (Open-Source Intelligence)** là quá trình thu thập thông tin từ các nguồn công khai và hợp pháp trên internet nhằm hỗ trợ các mục tiêu cụ thể, thường là điều tra hoặc giải quyết vấn đề. OSINT được ứng dụng trong nhiều lĩnh vực như an ninh mạng, điều tra pháp y, nghiên cứu thị trường và đặc biệt phổ biến trong các cuộc thi **CTF (Capture The Flag)**.

## 2. OSINT trong CTF là gì?
Trong CTF, **OSINT** thường là một thể loại bài thi mà người chơi cần thu thập thông tin công khai từ các nguồn khác nhau để giải các bài toán hoặc tìm "flag" (chuỗi ký tự xác nhận bạn đã giải đúng bài). 

OSINT trong CTF có thể yêu cầu bạn:
- Tìm thông tin cá nhân của một nhân vật giả định.
- Khám phá các chi tiết ẩn trong mạng xã hội, website hoặc cơ sở dữ liệu công khai.
- Truy tìm dấu vết của một hoạt động hoặc tài nguyên trên internet.

## 3. Các nguồn thu thập OSINT phổ biến
OSINT khai thác dữ liệu từ nhiều nguồn khác nhau, bao gồm:
- **Công cụ tìm kiếm**: Google, Bing, DuckDuckGo.
- **Mạng xã hội**: Facebook, Twitter, Instagram, LinkedIn.
- **Website và blog**: Trang chủ, trang giới thiệu, hoặc các bài đăng công khai.
- **WHOIS và DNS**: Tra cứu thông tin tên miền và máy chủ.
- **GitHub**: Tìm kiếm mã nguồn, tài liệu hoặc file nhạy cảm.
- **Cơ sở dữ liệu công khai**: Shodan, Censys, VirusTotal.
- **Metadata**: Dữ liệu ẩn trong ảnh, tài liệu hoặc file.

Geosint:
- **Google Image**
- **Google map**

## 4. Kỹ năng và công cụ hỗ trợ OSINT
### 4.1. Kỹ năng
- **Tìm kiếm nâng cao**: Biết sử dụng toán tử tìm kiếm trên Google như `site:`, `intitle:`, `filetype:`.
- **Phân tích dữ liệu**: Khả năng tổng hợp và suy luận từ các dữ liệu rời rạc.
- **Khả năng truy vết**: Tìm kiếm dấu vết trong metadata, logs, hoặc mạng xã hội.

### 4.2. Công cụ hỗ trợ
Dưới đây là một số công cụ phổ biến trong OSINT:
- **Google Dorking**: Tìm kiếm nâng cao trên Google.
- **Maltego**: Phân tích và vẽ sơ đồ mối quan hệ từ dữ liệu.
- **theHarvester**: Thu thập email, tên miền, và subdomain.
- **Recon-ng**: Khung công cụ cho OSINT với nhiều module.
- **ExifTool**: Phân tích metadata từ hình ảnh hoặc tài liệu.
- **Shodan**: Tìm kiếm các thiết bị kết nối internet.

## 5. Quy trình giải bài OSINT trong CTF
1. **Đọc kỹ đề bài**: Xác định từ khóa chính, thông tin ban đầu.
2. **Thu thập thông tin**: Sử dụng các công cụ và nguồn phù hợp để khai thác dữ liệu.
3. **Phân tích và tổng hợp**: Liên kết các dữ liệu rời rạc để tìm ra thông tin cần thiết.
4. **Xác minh thông tin**: Đảm bảo tính chính xác và hợp lệ của dữ liệu.
5. **Tìm flag**: Thông thường flag có dạng `CTF{...}` hoặc tương tự.
6. **Geosint**: Flag có thể chính là địa điểm cần osint

## 6. Ví dụ một bài OSINT cơ bản trong CTF

### 6.1. DeadSecCTF OSINT Challenge
- **Link**: [DeadSecCTF OSINT Challenge](https://h1n4mx0.github.io/posts/2024/07/deadsecctf/)
---
### 6.2. MTACTF OSINT Challenge
- **Link**: [MTACTF OSINT Challenge](https://h1n4mx0.github.io/posts/2024/08/mtactf/)
---
### 6.3. MSEC OSINT Challenge
- **Link**: [MSEC OSINT Challenge](https://h1n4mx0.github.io/posts/2024/12/msec-osint/)
---
### 6.4. CBJS OSINT Challenge
- **Link**: [CBJS OSINT Challenge](https://h1n4mx0.github.io/posts/2024/12/cbjs-osint/)
---
### Lời khuyên khi giải bài OSINT
- Đọc kỹ hướng dẫn từ các bài viết trên để hiểu quy trình giải quyết từng dạng bài.
- Rèn luyện kỹ năng sử dụng công cụ OSINT và nâng cao khả năng suy luận logic.
- Thử áp dụng các kỹ thuật này vào các bài OSINT khác để thực hành và cải thiện.


### Bonus
Một số nguồn osint để luyện tập:
[maverisolympic](https://2024.maverisolympics.fun/challenges)
[Tổng hợp Geosint của CyberSpace](https://cyberlances.wordpress.com/2021/07/02/tong-hop-cac-bai-osint-tren-cyber-space/)
