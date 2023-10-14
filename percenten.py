import streamlit as st
import urllib

st.title('％に化けた日本語URLを戻します！')
# 空白行の挿入
st.write('\n\n')
st.caption('日本語URLを貼り付けると%がいっぱいついた文字になりませんか？。<b>それを直します。</b>',unsafe_allow_html=True)
link = 'このサイトの関連情報は[イチゲブログ](https://kikuichige.com/)'
st.markdown(link, unsafe_allow_html=True)

with st.form(key='encode_form',clear_on_submit=True):
    url=st.text_input('戻したいURL（％が付いたURL）をここに貼ってください。',placeholder='例：https://kikuichige.com/%E3%83%97%E3%83%AD%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB/')
    st.text('変換を押すと日本語に戻します！')
    toukou_btn=st.form_submit_button('変換')

    if toukou_btn :

        if toukou_btn: 
            text=urllib.parse.unquote(url)
            st.write('戻しました！下のものをコピーしても%に文字化けしません。')
            st.write(text)

link = 'Excelなどで複数変換したいものがある場合など、ご相談ください。[Twitter](https://twitter.com/kikumel1)'
st.markdown(link, unsafe_allow_html=True)
