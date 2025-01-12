# Đôi điều về Reverse Engineering

## Reverse Engineering là gì?

Reverse Engineering (Kỹ thuật dịch ngược) là quá trình phân tích một sản phẩm đã hoàn thiện để tìm hiểu cách thức hoạt động, cấu trúc và nguyên lý của nó. Trong lĩnh vực phần mềm, Reverse Engineering thường được hiểu là việc phân tích các chương trình đã được biên dịch (file thực thi) để hiểu được logic, thuật toán và cách thức hoạt động của chương trình đó.

## Reverse Engineering trong CTF và thực tế

Trong các cuộc thi CTF (Capture The Flag), Reverse Engineering là một trong những chủ đề phổ biến và thú vị. Mục tiêu là giải đáp hoặc khai thác chương trình để thu được flag, thường là một chuỗi ký tự được dùng làm đáp án.
Các thử thách thường bao gồm:

- Phân tích Binary: Tìm hiểu cách chương trình hoạt động để tìm ra flag
- Crack Me: Vượt qua các cơ chế bảo vệ như serial key, password
- Anti-Debug: Đối phó với các kỹ thuật chống debug
- Malware Analysis: Phân tích mã độc (trong môi trường an toàn)

Ngoài CTF, Reverse Engineering còn được ứng dụng rộng rãi trong thực tế:

- Phát hiện malware: Phân tích mã độc hại để tìm hiểu cách nó lây lan và đánh giá mức độ nguy hiểm.
- Kiểm tra bảo mật: Đánh giá độ an toàn của các phần mềm hoặc thiết bị.
- Phát triển sản phẩm tương tự: Dùng Reverse Engineering để tái tạo lại các tính năng hoặc thiết kế từ một sản phẩm của người khác.
- Hỗ trợ khắc phục lỗi: Hiểu cách hệ thống hoạt động để xử lý các sự cố.

## Kiến thức nền tảng cần thiết

Reverse Engineering yêu cầu nền tảng kiến thức vững chắc trong nhiều lĩnh vực, bao gồm:

### 1. Kiến thức cơ bản

- Kiến thức ngôn ngữ lập trình: Thông thạo một vài ngôn ngữ như C, C++, Python...
- Kiến thức Assembly: Hiểu biết về Assembly để phân tích các chương trình biên dịch.
- Hệ điều hành: Kiến thức về cách hệ điều hành hoạt động (Windows, Linux...).
- Cơ chế bộ nhớ: Hiểu biết cách bộ nhớ được quản lý (stack, heap).

### 2. Kiến thức chuyên sâu

- File formats (PE, ELF)
- Quy trình biên dịch và linking
- Calling conventions
- Memory management
- API và System calls
- Các thuật toán mã hoá, hàm băm

### 3. Kỹ năng phân tích

- Đọc và hiểu assembly code
- Debugging techniques
- Pattern recognition
- Logic và thuật toán




## Setup hệ thống làm việc

### 1. Công cụ cơ bản

* Disassemblers và Decompilers: IDA Pro, Ghidra, Binary Ninja

* Debuggers: x64dbg/x32dbg (Windows), GDB (Linux), WinDbg, OllyDbg

* Công cụ phân tích động: Process Monitor, Process Explorer, Wireshark

### 2. Môi trường làm việc

* Hệ điều hành:
    * Windows (cho phân tích PE) Có thể sử dụng FlareVM
    * Linux (cho phân tích ELF) Có thể sử dụng REMNUX

* Các công cụ bổ trợ:

    * Python và các thư viện phân tích (pwntools, capstone)
    * Hex editors
    * Detect It Easy
    * PE-Bear
    * PEID
    * CFF Explorer
    * API Monitor

### 3. Tài nguyên học tập
Tài liệu tham khảo:
- "Practical Reverse Engineering" của Bruce Dang
- "Reversing: Secrets of Reverse Engineering" của Eldad Eilam
- "The IDA Pro Book" của Chris Eagle

### 4. Nền tảng thực hành:

- Crackmes.one
- Reverse Engineering challenges trên CTFtime
- Practice CTF platforms (HackTheBox, TryHackMe)
- Các bài RE có lời giải trên HackTheBox: https://hackmd.io/@0xMikiko/MainWriteups