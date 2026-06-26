import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database as db
from components.ui import avatar_html

def show():
    u = st.session_state.user
    st.markdown('<div class="page-title">💬 Messages</div>', unsafe_allow_html=True)

    inbox = db.get_inbox(u["id"])

    col_left, col_right = st.columns([1, 2])

    with col_left:
        st.markdown('<div class="section-header">Conversations</div>', unsafe_allow_html=True)

        if not inbox:
            st.markdown('<div style="color:#6B6B8A;font-size:0.85rem">No conversations yet.<br>Find peers and start chatting!</div>',
                        unsafe_allow_html=True)
        else:
            for contact in inbox:
                unread_badge = f' 🔴 {contact["unread"]}' if contact["unread"] else ""
                is_active = st.session_state.chat_with == contact["id"]
                style = "background:#6C63FF22;border:1px solid #6C63FF44;" if is_active else ""

                st.markdown(f"""
                <div style="display:flex;align-items:center;gap:8px;
                            background:#1C1C30;border:1px solid #2A2A45;
                            border-radius:8px;padding:0.6rem;margin-bottom:6px;
                            cursor:pointer;{style}">
                  {avatar_html(contact['full_name'] or contact['username'], contact['avatar_color'])}
                  <div>
                    <div style="font-size:0.88rem;font-weight:600;color:#E8E8F0">
                      {contact['full_name'] or contact['username']}{unread_badge}
                    </div>
                    <div style="font-size:0.75rem;color:#6B6B8A">@{contact['username']}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button("Open", key=f"open_chat_{contact['id']}", use_container_width=True):
                    st.session_state.chat_with = contact["id"]
                    st.rerun()

    with col_right:
        chat_uid = st.session_state.chat_with

        if not chat_uid:
            st.markdown("""
            <div style="text-align:center;padding:4rem;color:#6B6B8A">
              <div style="font-size:2.5rem">💬</div>
              <div>Select a conversation or find a peer to chat with</div>
            </div>""", unsafe_allow_html=True)
            return

        other = db.get_user_by_id(chat_uid)
        if not other:
            st.error("User not found.")
            return

        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;
                    background:#1C1C30;border:1px solid #2A2A45;
                    border-radius:10px;padding:0.8rem;margin-bottom:1rem">
          {avatar_html(other['full_name'] or other['username'], other['avatar_color'])}
          <div>
            <div style="font-weight:600;color:#E8E8F0">{other['full_name'] or other['username']}</div>
            <div style="font-size:0.78rem;color:#6B6B8A">@{other['username']}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Messages
        messages = db.get_conversation(u["id"], chat_uid)

        chat_html = '<div style="height:380px;overflow-y:auto;padding:0.5rem;margin-bottom:1rem">'
        if not messages:
            chat_html += '<div style="text-align:center;color:#6B6B8A;padding:2rem">No messages yet. Say hello! 👋</div>'
        else:
            for msg in messages:
                is_me = msg["sender_id"] == u["id"]
                bubble_class = "msg-sent" if is_me else "msg-recv"
                name = "You" if is_me else (other["full_name"] or other["username"])
                chat_html += f"""
                <div style="margin-bottom:8px">
                  <div style="font-size:0.72rem;color:#6B6B8A;margin-bottom:2px;
                              text-align:{'right' if is_me else 'left'}">{name}</div>
                  <div style="display:flex;justify-content:{'flex-end' if is_me else 'flex-start'}">
                    <div class="{bubble_class}">{msg['content']}</div>
                  </div>
                </div>"""
        chat_html += "</div>"
        st.markdown(chat_html, unsafe_allow_html=True)

        # Send
        with st.form("send_msg", clear_on_submit=True):
            col_input, col_btn = st.columns([5, 1])
            with col_input:
                msg_text = st.text_input("", placeholder="Type a message...", label_visibility="collapsed")
            with col_btn:
                send = st.form_submit_button("Send")
            if send and msg_text.strip():
                db.send_message(u["id"], chat_uid, msg_text.strip())
                st.rerun()