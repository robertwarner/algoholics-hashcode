class VideoServiceNetwork:
    def __init__(self, file):
        with open(file) as f:

            readline = lambda a: list(map(int, a.readline().split(' ')))

            self.num_videos, self.num_endpoints, self.num_requests, self.num_caches, self.cache_size = readline(
                f)

            self.video_size_list = readline(f)

            self.cache_connections = {i: [] for i in range(self.num_caches)}
            self.requests = [[] for i in range(self.num_endpoints)]
            for endpoint in range(self.num_endpoints):
                data_center_latency, num_cache_connections = readline(f)

                for _ in range(num_cache_connections):
                    cache_id, cache_latency = readline(f)

                    self.cache_connections[cache_id].append(
                        (endpoint, cache_latency - data_center_latency))
            for _ in range(self.num_requests):
                video_id, endpoint, requests_per_endpoint = readline(f)
                self.requests[endpoint].append(
                    (requests_per_endpoint, video_id))

        #print(self.cache_connections)
        #print(self.video_size_list)
        #print(self.requests)
