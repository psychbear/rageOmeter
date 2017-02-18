import json
from summonerCurrentGame import *


class InGameData:

	@staticmethod
	def getTargetSummonerData(summonerData, summonerName):
		currentGameSummoners = summonerData["participants"]
		targetData = []

		for summoner in currentGameSummoners:
			if summoner["summonerName"].lower().replace(' ', '') == summonerName:
				targetTeam = summoner["teamId"]
				targetChampionId = summoner["championId"]

				targetData.append(targetTeam)
				targetData.append(targetChampionId)

		return targetData

	@staticmethod
	def getEnemyTeamData(summonerData, targetSummonerTeamId):
		allEnemyData = []
		data = summonerData["participants"]

		for enemy in data:
			if enemy["teamId"] != targetSummonerTeamId:
				allEnemyData.append(enemy)

		return allEnemyData

	@staticmethod
	def Main():
		getLiveData = SummonerLiveData.Main()
		summonerName = getLiveData[0]
		rawData = getLiveData[1]

		if "status" in rawData:
			print "Summoner not in game."	
		else:
			targetSummonerData = InGameData.getTargetSummonerData(rawData, summonerName)
			print targetSummonerData

			enemyData = InGameData.getEnemyTeamData(rawData, targetSummonerData[0])
			print enemyData

if __name__ == "__main__":

	InGameData.Main()