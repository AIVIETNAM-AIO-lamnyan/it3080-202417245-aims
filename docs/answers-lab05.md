# Lab 05 – Câu hỏi thảo luận

## Ưu, nhược điểm của upstream first so với release first?

Upstream first sửa lỗi trên nhánh phát triển chính trước, rồi cherry-pick
bản sửa sang các nhánh release bị ảnh hưởng. Cách này giúp lỗi được sửa
một lần ở nguồn chính và các phiên bản sau nhận được bản sửa sớm; đổi lại,
các nhánh release có thể phải chờ bản sửa được kiểm thử và tích hợp ở
upstream.

Release first sửa trực tiếp từ baseline phát hành, nên có thể đưa bản vá
cho khách hàng nhanh và cô lập thay đổi riêng cho phiên bản cũ. Tuy nhiên,
cần chủ động lan truyền bản sửa sang `main` và các release khác; nếu quên,
các phiên bản sẽ lệch nhau.

## Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào phát hiện?

`git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`
kiểm tra các bản cherry-pick theo dấu truy vết. Ngoài ra,
`git cherry -v origin/main origin/release/lab05` cho thấy các commit tương
đương còn thiếu hoặc đã có giữa hai nhánh.
