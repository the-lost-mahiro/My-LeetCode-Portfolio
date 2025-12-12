class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        status = [0] * numberOfUsers
        events.sort(key = lambda x: (int(x[1]), 0 if x[0] == 'OFFLINE' else 1))
        
        for event, time, id in events:
            if event == 'OFFLINE':
                status[int(id)] = int(time) + 60
            if event == 'MESSAGE':
                if id == 'ALL':
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif id == 'HERE':
                    for i in range(numberOfUsers):
                        if status[i] <= int(time):
                            mentions[i] += 1
                else:
                    id = id.split()
                    for i in id:
                        mentions[int(i[2:])] += 1
                    
        return mentions                
