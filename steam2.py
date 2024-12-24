import streamlit as st
import pandas as pd
label = pd.DataFrame({'columns1':[1,2,3,4,5,6,7],"column2":[11,12,13,14,15,16,17]})
# st.markdown("""
# <style>
#
# .st-emotion-cache-h4xjwg {
#         visibility:hidden;
# }
# </style>
# """,unsafe_allow_html= True)
st.markdown("""
        <style>
        .st-emotion-cache-h4xjwg{
        position:static;
        }
        .st-emotion-cache-13k62yr{
        display:flex;
        justify-content: center;
        align-items: center;
        background: url('https://png.pngtree.com/thumb_back/fw800/background/20240607/pngtree-digital-human-brain-with-blue-light-emitting-from-base-image_15861367.jpg') no-repeat;
        background-size: cover;
        background-position: center;
}
        .st-emotion-cache-1dp5vir{
        visibility:hidden;
        }
        </style>
 """,unsafe_allow_html = True)
#
st.title("title Hi I am Mostafa Mahmoud")
st.header("i am header")
st.subheader("Hi SubHeader")
st.text("Text Mostafa Genesh")

## italic and bold fonts
st.markdown("**Hello** *world*") # when i want it bold i make it in double astiric and if make a single star will make it atlic

## Headers
st.markdown(" # H1")
st.markdown("## H2")
st.markdown("### H3")
st.markdown("#### H4")
st.markdown("##### H5")
st.markdown("###### H6")

## ordered List
st.markdown("> blockquote")
st.markdown("1. First item")
st.markdown("2. Second item")
st.markdown("3. third item")

## unorderd List
st.markdown("- First item")
st.markdown("- Second item")
st.markdown("- third item")

## code
st.markdown("`int x = 5`")

## Horizontal Rule
st.markdown("---")

## Link
st.markdown("[Facebook](https://www.facebook.com)")

## Image
st.markdown("![alt text](data:image/jpeg;base64,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)")

## caption
st.caption("Hi I am caption")

## how to write matrix
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

## print variables
json = {"a":[1,2,3,4],
        "b":"2,4,3,2",
        "c":3}
st.json(json)
code = """
Value = 5
print("hello world")
def function():
    return Value
"""
st.code(code,language="python")

st.write("## h2")
##
st.metric(label="wind Speed" , value = "120ms",delta="1.4ms")
st.metric(label="wind Speed" , value = "120ms",delta="-1.4ms")
st.table(label)
st.dataframe(label)
st.image("29099.jpg",caption="this my image",width=600)
# st.audio("audio.mp3")
st.video("notebook8e979138fe _ Kaggle - Google Chrome 2024-12-10 21-39-48.mp4")
def change():
        print("Changed")
        print(st.session_state.check)
state = st.checkbox("what are you favorite?",value=True,on_change=change,key="check")
if state:
        st.write("Yabha ahla msa alic")
radio_btn = st.radio("***Where are you live?***",options=("USA","EGY","KSA"))
st.markdown(radio_btn)
def clickk():
        print("Click")
st.button("Click me!!",on_click=clickk)
# def chan():
#         # print(st.session_state.kl)
#         st.markdown(select)
select = st.selectbox("whats your favorite car?",options=("Nissan","Lada","Mercedes Benz"))
st.markdown(f"#### *My Favorite Car : {select}*")
list1 = ["Apple","Samsung","Realme","Oppo"]
multi = st.multiselect("whats your favorite Companies?",options=(list1))
# st.markdown(f"#### *My Favorite Companies : {multi}*")
# for i in multi:
# for i in range(len(multi)):
#         ui = f"{multi[i]},"
# print(ui.)
ui = ""
for i in range(len(multi)):
        li = multi[i]
        ui = ui + li+","
# print(list1[0],list1[1])
# ui = ui.(ui,1,len(ui))
print(ui)
print(f"My Favorite Companies : {ui[:len(ui)-1]}")
# print(f"Mostafa{select}")
