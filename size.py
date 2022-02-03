import sys
import cv2
from elice_utils import EliceUtils

elice_utils = EliceUtils()


# 주어진 영상과 조각 순서를 보고 원본 영상(출력 예시 참고)으로 복원한 영상을 반환하는 함수를 구현하세요.
def solve_puzzle(img, piece_order):
    for to_idx, from_idx in enumerate(piece_order):
        if to_idx == from_idx:
                continue
            
        proper_idx = piece_order.index(to_idx)
        piece_order[to_idx] = piece_order[proper_idx]
        piece_order[proper_idx] = from_idx
        
        r, c = img.shape[0] //2, img.shape[1] //2
        p1 = tuple(map(lambda x : x*r, divmod(from_idx, 2)))
        p2 = tuple(map(lambda x : x*r, divmod(to_idx, 2)))
        
        tmp = img[p1[0]:p1[0] + r, p1[1]:p1[1] + c].copy()
        img[p1[0]:p1[0] + r, p1[1]:p1[1] + c] = img[p2[0]:p2[0] + r, p2[1]:p2[1] + c]
        
        img[p2[0]:p2[0] + r, p2[1]:p2[1] + c] = tmp[:]

        

    return img
    

if __name__ == "__main__":
    # 퍼즐의 순서가 리스트 형태로 입력됩니다.
    piece_order = list(map(int, list(sys.argv[1].split(','))))
    
    # 이미지를 불러옵니다.
    img = cv2.imread("./puzzle.jpg", cv2.IMREAD_GRAYSCALE)
    
    # 복원 결과를 확인합니다.
    result_img = solve_puzzle(img, piece_order)
    cv2.imwrite('result.jpg', result_img) 
    elice_utils.send_image('result.jpg')
