from channels.consumer import AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer
import asyncio
from asgiref.sync import async_to_sync
import json
from chat.models import Group_names ,Participants,Chat
from channels.db import database_sync_to_async

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        #print('connect')
        #print ('channel layer...',self.channel_layer)
        #print('groupId Final..',self.scope['url_route']['kwargs']['group_id'])
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        #print(group_name)

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self,event):
        print('receive for clint',event['text'])
        data=json.loads(event['text'])
        id=(data['p_id'])
        p_id=str(id)
        msg=data['msg']
        group_id=self.group_name
        print(group_id)
        chat=Chat(
            msg=msg,
            group_id=group_id,
            participant_id=p_id,
        )
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(
            self.group_name,
            {
            'type':'chat.message',
            'message':event['text'],
            
            
            }
        )
    async def chat_message(self,event):
        #print('actual data',event['text'])
        await self.send({
            'type':'websocket.send',
            'text':event['message'],
        })
 
    async def websocket_disconnect(self,event):
        #print('disconnect')
        await self.channel_layer.group_discard(self.group_name,self.channel_name)
        raise StopConsumer()