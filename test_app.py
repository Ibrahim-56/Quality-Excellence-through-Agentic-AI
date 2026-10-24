import unittest

from app import MonitoringAgent, QualityMetric, RecommendationAgent


class MonitoringAgentTests(unittest.TestCase):
    def test_flags_metrics_below_threshold(self):
        metrics = [
            QualityMetric("Customer Satisfaction", 82, 90),
            QualityMetric("SLA Compliance", 95, 90),
        ]

        alerts = MonitoringAgent().analyze(metrics)

        self.assertEqual(alerts, ["Alert: Customer Satisfaction"])

    def test_no_alerts_when_all_metrics_meet_threshold(self):
        metrics = [
            QualityMetric("Customer Satisfaction", 90, 90),
            QualityMetric("SLA Compliance", 95, 90),
        ]

        self.assertEqual(MonitoringAgent().analyze(metrics), [])


class RecommendationAgentTests(unittest.TestCase):
    def test_creates_recommendations_for_alerts(self):
        alerts = ["Alert: Customer Satisfaction"]

        recommendations = RecommendationAgent().recommend(alerts)

        self.assertEqual(
            recommendations,
            ["Investigate and improve: Alert: Customer Satisfaction"],
        )


if __name__ == "__main__":
    unittest.main()
