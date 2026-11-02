# Lab 01 – Câu hỏi thảo luận

## Vì sao dùng `git mv`?

`git mv` đổi tên hoặc di chuyển tệp và đưa thay đổi vào staging. Git lưu
thay đổi nội dung theo từng đường dẫn, không lưu thao tác đổi tên riêng;
GitHub nhận diện tệp được di chuyển dựa trên mức độ giống nhau giữa bản
cũ và bản mới. Vì vậy, lịch sử tệp vẫn có thể được theo dõi sau refactor.

## `release/lab01` có phải baseline không?

Có. Nhánh này đánh dấu phiên bản đã nộp của Lab 01, được tạo từ `main`
sau khi PR refactor được merge. Tại thời điểm tạo, hai nhánh trỏ tới cùng
một commit; nhánh release giúp tra cứu và tái tạo trạng thái bài nộp về sau.

## Vì sao không commit thẳng vào `main` dù làm một mình?

Nhánh riêng và PR giữ `main` ổn định, cô lập thay đổi, đồng thời duy trì
quy trình review và kiểm tra giống khi làm nhóm. Cách này cũng giúp lịch sử
thay đổi rõ ràng và dễ xử lý nếu cần hoàn tác.

## Cấu hình `--global` khác `--local` thế nào?

Cấu hình `--global` nằm trong cấu hình người dùng (thường là
`%USERPROFILE%\.gitconfig` trên Windows) và áp dụng cho các repository của
tài khoản đó. Cấu hình `--local` nằm trong `.git/config`, chỉ áp dụng cho
repository hiện tại và được ưu tiên hơn cấu hình global khi cùng một khóa
được đặt ở cả hai nơi.
