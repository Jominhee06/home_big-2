using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Control : MonoBehaviour
{
    // 룰렛을 돌리는 속도
    float rotationSpeed = 0;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        // 2D인데 돌리는 축은 z 축이라서 변수명을 넣어줌
        transform.Rotate(0,0,rotationSpeed);
        // 돌아가는 속도를 점점 줄여서 멈추기
        rotationSpeed *= 0.996f;
        // 마우스 버튼을 누르면 6의 속도로 돌려라
        if(Input.GetMouseButtonDown(0))
        {
            rotationSpeed = 6;
        }
    }
}
