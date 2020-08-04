from input_parser import VideoServiceNetwork
import math


def packing(f):
    graph = VideoServiceNetwork(f)
    cachelist = [set() for _ in range(graph.num_caches)]
    for cache in graph.cache_connections:
        print(f'selecting cache: {cache} out of {graph.num_caches}')
        size = graph.cache_size
        while (size != 0):
            savings = math.inf
            video_id = -1
            endpoint = -1
            request_per_endpoint = -1
            # check endpoints connected to cache
            for e_list in graph.cache_connections[cache]:
                # loop through requests at endpoint
                if not graph.requests[e_list[0]]:
                    continue
                for request in graph.requests[e_list[0]]:
                    # check if video will fit
                    if request[1] not in cachelist[
                            cache] and graph.video_size_list[
                                request[1]] <= size:
                        temp = request[0] * e_list[1]
                        if temp < savings:
                            savings = temp
                            video_id = request[1]
                            endpoint = e_list[0]
                            request_per_endpoint = request[0]

            if video_id == -1:
                break
            size -= graph.video_size_list[video_id]
            graph.requests[endpoint].remove((request_per_endpoint, video_id))
            cachelist[cache].add(video_id)
    return cachelist


def CreateOutputFile(cache_video_list):
    used_cache = []
    cache_counter = 0
    for id, cache in enumerate(cache_video_list):
        if cache:
            cache_counter += 1
            d = list(cache)
            d.insert(0, id)
            used_cache.append(d)
    f = open("./outputs/music_videos_of_2020.out", "w")
    f.write(str(cache_counter) + '\n')
    for c in used_cache:
        f.write(" ".join(list(map(str, c))))
        f.write('\n')
    f.close()


if __name__ == '__main__':
    CreateOutputFile(packing('./data/music_videos_of_2020.in'))
