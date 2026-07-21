from dataclasses import dataclass

@dataclass
class QualityMetric:
    name:str
    value:float
    threshold:float

class MonitoringAgent:
    def analyze(self, metrics):
        return [f"Alert: {m.name}" for m in metrics if m.value < m.threshold]

class RecommendationAgent:
    def recommend(self, alerts):
        return [f"Investigate and improve: {a}" for a in alerts]

def main():
    metrics=[QualityMetric("Customer Satisfaction",82,90), QualityMetric("SLA Compliance",95,90)]
    alerts=MonitoringAgent().analyze(metrics)
    recs=RecommendationAgent().recommend(alerts)
    print("=== Quality Dashboard ===")
    for a in alerts: print(a)
    for r in recs: print(r)

if __name__=='__main__':
    main()
