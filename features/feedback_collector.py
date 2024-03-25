import json

class FeedbackCollector:
    def __init__(self, db):
        self.db = db

    def collect_feedback(self, session_id, feedback):
        """
        Stores feedback from a chat session.

        Args:
            session_id (str): The unique identifier for the chat session.
            feedback (dict): A dictionary containing feedback details.

        Returns:
            bool: True if feedback is stored successfully, False otherwise.
        """
        if not session_id or not feedback:
            print("Session ID and feedback are required.")
            return False

        try:
            feedback_record = {
                "session_id": session_id,
                "feedback": json.dumps(feedback),
                "timestamp": datetime.now()
            }
            self.db.insert_feedback(feedback_record)
            return True
        except Exception as e:
            print(f"Error collecting feedback: {e}")
            return False
