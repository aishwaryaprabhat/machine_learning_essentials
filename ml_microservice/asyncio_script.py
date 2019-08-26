import asyncio
import logging
import aiohttp

FORMAT = '[%(asctime)-15s][%(levelname)-8s]%(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Starting Example")

async def get_model(model_name, time_to_sleep):

	logger.info('[get_model][{}] Calling microservice'.format(model_name))
	await asyncio.sleep(time_to_sleep)
	logger.info('[get_model][{}] Returns result'.format(model_name))




async def do_request(url):

	logger.info('[do_request][{}] Calling web'.format(url))
	response = await aiohttp.request('GET',url)
	logger.info('[do_request][{}] Return result:{}'.format(url,response.status))

	return response


if __name__=='__main__':

	loop = asyncio.get_event_loop()

	# loop.run_until_complete((asyncio.gather(
	# 						get_model("Model A",2),
	# 						get_model("Model B",1)
	# 						)))

	loop.run_until_complete((asyncio.gather(
							do_request("http://www.fakeresponse.com/api/?sleep=1"),
							do_request("http://google.sg")
							)))

	loop.close()

