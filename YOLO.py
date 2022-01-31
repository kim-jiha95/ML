import cv2
import tensorflow as tf
from yolov3.models import YoloV3Tiny

from yolov3.dataset import transform_images
from yolov3.utils import draw_outputs


from answer import answer


def convert_outputs(outputs):
    ret_boxes, ret_scores, ret_classes = [], [], []

    boxes, scores, classes, nums = outputs
    boxes, scores, classes, nums = list(boxes[0]), list(scores[0]), list(classes[0]), nums[0]

    for i in range(nums):
        box, score, class_idx = boxes[i], scores[i], classes[i]
        ret_boxes.append(box)
        ret_scores.append(score)
        ret_classes.append(class_names[class_idx])

    return ret_boxes, ret_scores, ret_classes


if __name__ == '__main__':
    class_names = [c.strip() for c in open('./coco.names').readlines()]
    yolo = YoloV3Tiny(classes=len(class_names))
    yolo.load_weights('./checkpoints/yolov3-tiny.tf')

    vid = cv2.VideoCapture("cam5.avi")

    falldown_start, falldown_end = 0, 0
    frame_number = 0

    while vid.isOpened():
        _, img = vid.read()

        if img is None:
            continue

        img_in = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_in = tf.expand_dims(img_in, 0)
        img_in = transform_images(img_in, 416)
        boxes, scores, classes = convert_outputs(yolo.predict(img_in))
        color = (255, 0, 0)
        
        """
        boxes에는 박스의 (x1,y2), (x2,y2) 좌표가 실수로 있습니다.
        scores에는 박스의 confidence 값이 있고, classes에는 str타입에 박스의 클래스 이름이 있습니다.
        여러분들이 자유롭게 생각하여 객체 감지를 이용한 행동 인식을 수행해봅시다.
        """
        
        cv2.putText(img, f"{frame_number}",(20, 20),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
                    
        for box, score, class_name in zip(boxes, scores, classes):
            box[0] *= img.shape[1]
            box[1] *= img.shape[0]
            box[2] *= img.shape[1]
            box[3] *= img.shape[0]
            cv2.rectangle(img, (int(box[0]), int(box[1])),
                               (int(box[2]), int(box[3])), color, 2)
            cv2.putText(img, f"{class_name} {score:.3f}",
                        (int(box[0]), int(box[1])),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)

        frame_number += 1
        cv2.imshow('output', img)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
    
    # 정답을 출력합니다.
    answer(falldown_start, falldown_end)
