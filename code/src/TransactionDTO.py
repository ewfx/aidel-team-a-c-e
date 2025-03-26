from typing import List
class TransactionDTO:
               transactionID: str
               extractedEntities: List[str] = []
               entityType: List[str] = []
               riskScore: float
               supportingEvidence: List[str] = []
               confidenceScore: float
               reason: str

               def __init__(self, transactionID, extractedEntities, entityType, riskScore, supportingEvidence, confidenceScore, reason):
                              self.transactionID = transactionID
                              self.extractedEntities = extractedEntities
                              self.entityType = entityType
                              self.riskScore = riskScore
                              self.supportingEvidence = supportingEvidence
                              self.confidenceScore = confidenceScore
                              self.reason = reason
