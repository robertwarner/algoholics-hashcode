class VideoServiceNetwork:
    def __init__(self, file):
        read_one_line = lambda f: list(map(int, f.readline().split(' ')))

        with open(file) as f:
            self.num_videos, self.num_endpoints, self.num_requests, self.num_caches, self.cache_size = read_one_line(f)
            self.video_size_list = read_one_line(f)
            self.endpoint_graph = {
                i: [[], []]
                for i in range(self.num_endpoints)
            }
            for endpoint in range(self.num_endpoints):
                data_center_latency, endpoint_caches = read_one_line(f)
                for e in range(endpoint_caches):
                    cache_id, cache_latency = read_one_line(f)
                    self.endpoint_graph[endpoint][0].append(
                        (data_center_latency - cache_latency, cache_id))

            self.greedy_list = []            
            for request_id in range(self.num_requests):
                video_id, endpoint, requests_per_endpoint = read_one_line(f)
                self.endpoint_graph[endpoint][1].append(
                    (requests_per_endpoint, video_id))
                for saved_latency, cache_id in self.endpoint_graph[endpoint][0]:
                    self.greedy_list.append(
                        (requests_per_endpoint * saved_latency / self.video_size_list[video_id], cache_id, video_id, request_id))
