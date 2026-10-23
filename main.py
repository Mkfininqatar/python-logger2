from datetime import datetime
from typing import List, Tuple
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Hamad-Tamim Global Dignity & Telemetry Framework (HT-MTF)",
    version="1.0.0",
    description="National Digital Labor Governance, Telemetry, and Sovereign Anti-Exploitation Pipeline."
)

# --- Sample Core Models for Testing ---
class WeatherAutoShutdown(BaseModel):
    site_id: str
    current_ambient_temp_celsius: float
    max_safe_temp_threshold: float = 40.0
    is_outdoor_work_permitted: bool = True
    shutdown_trigger_reason: str = "NORMAL_OPERATIONS"

    def evaluate_weather_safety(self):
        if self.current_ambient_temp_celsius > self.max_safe_temp_threshold:
            self.is_outdoor_work_permitted = False
            self.shutdown_trigger_reason = "EXTREME_HEAT_SHUTDOWN_ENFORCED"
        else:
            self.is_outdoor_work_permitted = True
            self.shutdown_trigger_reason = "NORMAL_OPERATIONS"

class AntiPaperworkFraudBlocker(BaseModel):
    audit_report_id: str
    site_id: str
    submitted_paperwork_claims: dict
    sensor_telemetry_ground_truth: dict
    is_audit_approved: bool = True
    rejection_reason: str = "CLEAN"

    def evaluate_audit(self):
        reported_hours = self.submitted_paperwork_claims.get("reported_work_hours", 0)
        actual_hours = self.sensor_telemetry_ground_truth.get("actual_work_hours", 0)
        if actual_hours > (reported_hours + 1.0):
            self.is_audit_approved = False
            self.rejection_reason = "FRAUD_DETECTED_HIDDEN_OVERTIME"
        else:
            self.is_audit_approved = True
            self.rejection_reason = "APPROVED"

class ConfinedLaborAlert(BaseModel):
    camp_or_site_id: str
    qid: str
    last_known_gps: Tuple[float, float]
    is_illegally_confined: bool = False
    confinement_alert_triggered: str = "NORMAL_MOVEMENT"

# --- API Endpoints ---
@app.get("/", tags=["System Status"])
def read_root():
    return {
        "framework": "Hamad-Tamim Global Dignity & Telemetry Framework",
        "status": "SECURE_ACTIVE_MONITORING",
        "total_active_points_governed": 30
    }

@app.post("/api/v1/compliance/evaluate-site", tags=["Automated Compliance Engine"])
def evaluate_site_telemetry(
    weather_sensor: WeatherAutoShutdown,
    fraud_blocker: AntiPaperworkFraudBlocker,
    confinement_check: ConfinedLaborAlert
):
    weather_sensor.evaluate_weather_safety()
    fraud_blocker.evaluate_audit()
    
    return {
        "site_id": weather_sensor.site_id,
        "weather_status": weather_sensor.shutdown_trigger_reason,
        "outdoor_permitted": weather_sensor.is_outdoor_work_permitted,
        "audit_approval": fraud_blocker.is_audit_approved,
        "audit_reason": fraud_blocker.rejection_reason,
        "timestamp": datetime.utcnow().isoformat()
    }