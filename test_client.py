import httpx

BASE_URL = "http://127.0.0.1:8000"
HEADERS = {"X-API-Key": "HT-MTF-SECURE-SOVEREIGN-KEY-2026"}

def test_secure_evaluation():
    payload = {
        "weather_sensor": {
            "site_id": "SITE_DOHA_HPC_01",
            "current_ambient_temp_celsius": 43.0,
            "max_safe_temp_threshold": 40.0,
            "is_outdoor_work_permitted": True,
            "shutdown_trigger_reason": "NORMAL_OPERATIONS"
        },
        "fraud_blocker": {
            "audit_report_id": "AUDIT_8851",
            "site_id": "SITE_DOHA_HPC_01",
            "submitted_paperwork_claims": {"reported_work_hours": 8.0},
            "sensor_telemetry_ground_truth": {"actual_work_hours": 10.5},
            "is_audit_approved": True,
            "rejection_reason": "PENDING"
        },
        "hpc_node": {
            "node_id": "QNV-HPC-NODE-09",
            "cpu_utilization_percent": 91.5,
            "gpu_temperature_celsius": 78.4,
            "cluster_power_draw_kw": 45.2,
            "is_telemetry_healthy": True
        }
    }
    
    response = httpx.post(f"{BASE_URL}/api/v1/compliance/evaluate-site", json=payload, headers=HEADERS)
    print("Secure Response:", response.json())

if __name__ == "__main__":
    test_secure_evaluation()