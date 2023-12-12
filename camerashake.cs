using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class cameraShakeController : MonoBehaviour
{   
    public Transform cameraTransform = default;
    private Vector3 _orignalPosOfCam = default;
    public float shakeFrequency = default;
    void Start()
    {
        _orignalPosOfCam = cameraTransform.position;
    }

    void Update()
    {
        if (Input.GetKey(KeyCode.S))
        {
            CameraShake();
        }
        else if (Input.GetKeyUp(KeyCode.S))
        {
            StopShake();
        }
    }
    private void CameraShake()
    {
        cameraTransform.position = _orignalPosOfCam + Random.insideUnitSphere *
        shakeFrequency;
    }
    private void StopShake()
    {
        cameraTransform.position = _orignalPosOfCam;
    }
}
