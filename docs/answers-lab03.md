# Lab 03 – Câu hỏi thảo luận

## Merge base là gì?

Merge base là tổ tiên chung gần nhất của hai nhánh cần hợp nhất. Git dùng
commit này làm điểm tham chiếu để so sánh phần thay đổi trên mỗi nhánh và
tạo kết quả merge ba chiều. Nếu hai nhánh sửa cùng một vùng theo cách
không thể tự kết hợp, Git yêu cầu giải quyết conflict.

## Vì sao `main` và `release/*` nên dùng `revert`?

Đây là các nhánh có lịch sử đã chia sẻ. `git revert` tạo commit mới đảo
ngược thay đổi nhưng giữ nguyên các commit cũ, giúp cộng tác viên đồng bộ
lịch sử an toàn và vẫn truy vết được quyết định đã tích hợp. `reset` di
chuyển con trỏ nhánh và có thể viết lại lịch sử mà người khác đã lấy về;
vì vậy chỉ nên dùng cho commit riêng, chưa chia sẻ.
