css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    border: 1px solid black;
    

}
.chat-message.bot {
    border: 1px solid black;
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: black;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="C:/Users/win10/OneDrive/Desktop/chatpdf/img/image_bot.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="./img/image_bot.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

