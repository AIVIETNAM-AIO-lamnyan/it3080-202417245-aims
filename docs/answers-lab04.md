# Lab 04 – Câu hỏi thảo luận

## Vì sao `release/*` không merge ngược vào `main` trong flow này?

`release/*` đóng băng một baseline đã phát hành để có thể kiểm toán và tái
tạo chính xác. Phát triển thông thường tiếp tục trên `main`; nếu có sửa lỗi
cần đưa sang các dòng phiên bản, thay đổi được truyền có chủ đích bằng
hotfix hoặc cherry-pick. Cách này tránh đưa nhầm các thay đổi chỉ dành cho
một bản phát hành cũ vào dòng phát triển chính.

## Flow này khác GitFlow thế nào?

GitFlow truyền thống có các nhánh `develop`, `release/*` và `hotfix/*`;
nhánh release thường được merge trở lại `develop` và `main` khi phát hành.
Flow của bài lab dùng `main` làm dòng phát triển chính, còn `release/*`
được giữ như baseline bất biến; hotfix được lan truyền tường minh giữa
các nhánh bị ảnh hưởng.

## Vì sao phát hành `1.0.0` thay vì `0.4.0`?

Theo Semantic Versioning, phiên bản `1.0.0` biểu thị sản phẩm đã có API
công khai ổn định và cam kết tương thích. `0.4.0` vẫn thuộc giai đoạn
phát triển ban đầu, khi API có thể thay đổi không tương thích mà chưa cần
tăng số phiên bản MAJOR.
