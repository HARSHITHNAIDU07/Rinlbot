import http.client
import json

conn = http.client.HTTPConnection("10.9.162.21", 11434)

while(True):
    prompt=input("Enter the prompt")
    if(prompt=="0"):
         break
    else:
        payload = {
            "model": "rinlbot",
            "messages": [
                {"role": "user", "content":prompt+" Answer in less than 30 words"}
            ]
        }

        headers = {
            "Content-Type": "application/json"
        }

        conn.request("POST", "/api/chat", body=json.dumps(payload), headers=headers)

        response = conn.getresponse()
        data = response.read()



        json_objects = data.decode("utf-8").split('\n')


        messages = [json.loads(obj)['message']['content'] for obj in json_objects if obj.strip()]


        output_string = ''.join(messages)

        print(output_string)

conn.close()
