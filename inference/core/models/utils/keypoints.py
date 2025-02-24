from typing import List

from inference.core.entities.responses.inference import Keypoint
from inference.core.exceptions import ModelArtefactError


def superset_keypoints_count(keypoints_metadata={}) -> int:
    """Returns the number of keypoints in the superset."""
    max_keypoints = 0
    for keypoints in keypoints_metadata.values():
        if len(keypoints) > max_keypoints:
            max_keypoints = len(keypoints)
    return max_keypoints


def model_keypoints_to_response(
    keypoints_metadata: dict,
    keypoints: List[float],
    predicted_object_class_id: int,
    keypoint_confidence_threshold: float,
) -> List[Keypoint]:
    if keypoints_metadata is None:
        raise ModelArtefactError("Keypoints metadata not available.")

    keypoint_id2name = keypoints_metadata[predicted_object_class_id]
    num_keypoints = len(keypoints) // 3
    num_names = len(keypoint_id2name)

    results = []
    for keypoint_id in range(min(num_keypoints, num_names)):
        offset = 3 * keypoint_id
        confidence = keypoints[offset + 2]
        if confidence >= keypoint_confidence_threshold:
            keypoint = Keypoint(
                x=keypoints[offset],
                y=keypoints[offset + 1],
                confidence=confidence,
                class_id=keypoint_id,
                **{"class": keypoint_id2name[keypoint_id]},
            )
            results.append(keypoint)

    return results
