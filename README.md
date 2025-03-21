# 🖼️ Cartoon Filter

## 🎯 설명
컴퓨터 비전 기술을 활용해 일반 이미지를 만화 스타일로 변환하는 Cartoon Filter 입니다.

---

## 🧠 알고리즘 요약

- **엣지(윤곽선) 검출**: Canny Edge Detection을 사용해 선명한 윤곽선 추출
- **윤곽선 강조**: 엣지를 반전하고 팽창시켜 만화의 잉크 선 느낌 구현
- **색상 단순화**: K-means 클러스터링을 통해 색상 수를 줄여 만화처럼 단순한 색감 제공
- **블러 처리**: Bilateral Filter를 사용하여 색상 경계를 부드럽게 표현
- **결합**: 윤곽선과 색상 이미지를 `bitwise_and`로 합성하여 최종 카툰 스타일 이미지 생성

---

## 📸 데모 이미지

| Original | Cartoon |
|----------|---------|
| ![Original](./Demo_Image/Cat_Original.png) | ![Cartoon](./Demo_Image/Cat_Cartoon.png) |
