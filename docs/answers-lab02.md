# Lab 02 – Câu hỏi thảo luận

## Vì sao phải đồng bộ `main` trước khi tạo PR?

Đồng bộ nhánh tính năng với `main` giúp phát hiện sớm xung đột và lỗi tích
hợp trên phiên bản mới nhất. Nhờ vậy, người review có thể đánh giá thay đổi
trong đúng bối cảnh mà PR sẽ được merge, thay vì phát hiện vấn đề sau đó.

## Khi nào không được rebase?

Không nên rebase các commit đã push và đang được người khác dùng chung:
rebase tạo lại commit với SHA khác, khiến lịch sử nhánh bị viết lại và có
thể buộc cộng tác viên phải đồng bộ hoặc giải quyết xung đột lại. Với lịch
sử đã chia sẻ, nên dùng merge hoặc `git revert` tùy mục đích.

## `feature/*` khác `topic/*` ra sao?

`feature/*` thường chứa thay đổi chức năng hướng tới người dùng, như in
nội dung giỏ hàng hoặc tìm DVD theo tiêu đề. `topic/*` thường gom một chủ
đề kỹ thuật hoặc tài liệu hỗ trợ quy trình, như mẫu PR hay sơ đồ use case.
