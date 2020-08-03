class VideoServiceNetwork:
    def __init__(self, file):
        with open(file) as f:
            self.num_videos, self.num_endpoints, self.num_requests, self.num_caches, self.cache_size = list(
                map(int,
                    f.readline().split(' ')))
            self.video_size_list = list(map(int, f.readline().split(' ')))
            self.endpoint_graph = {
                i: [[], []]
                for i in range(self.num_endpoints)
            }
            for endpoint in range(self.num_endpoints):
                data_center_latency, endpoint_caches = list(
                    map(int,
                        f.readline().split(' ')))
                self.endpoint_graph[endpoint][0].append(
                    (data_center_latency, -1))
                #TODO(rwarner): Possibly save differences between datacenter and caches
                for e in range(endpoint_caches):
                    cache_id, cache_latency = list(
                        map(int,
                            f.readline().split(' ')))
                    self.endpoint_graph[endpoint][0].append(
                        (cache_latency, cache_id))
            for _ in range(self.num_requests):
                video_id, endpoint, requests_per_endpoint = list(
                    map(int,
                        f.readline().split(' ')))
                self.endpoint_graph[endpoint][1].append(
                    (requests_per_endpoint, video_id))
