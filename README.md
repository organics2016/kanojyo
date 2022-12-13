# kanojyo

基于 [OpenAI GPT-3](https://beta.openai.com/docs/models) 和 [Microsoft TTS](https://azure.microsoft.com/zh-cn/products/cognitive-services/text-to-speech/#features) 的智能语音助理，你可以用麦克风和她对线。

## Runtime

- 一个正常工作的麦克风和扬声器 (没麦怎么对线？)
- Windows 10 or last (Linux 或 macOS 大概可以但我没试过)
- Python 3.7.x or last (Python 3.11.0 跑了没啥问题)
- 一个 Microsoft Azure 账号
- 一个 OpenAI 账号

## Dependencies

- azure.cognitiveservices.speech
- openai


## Quickstart

1. Clone this repository
```
git clone https://github.com/organics2016/kanojyo.git
```

2. 安装依赖
```
pip install azure.cognitiveservices.speech
```
```
pip install openai
```

3. 编辑配置文件
    - 项目中有一个 `config.ini.example` 配置文件，改名或复制为 `config.ini`
    - Microsoft TTS 地区和key怎么填? 需要你在Azure下建立语音服务资源，然后获取地区和key [详细看这里](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started-speech-to-text?tabs=windows%2Cterminal&pivots=programming-language-python#prerequisites)
    - OpenAI key怎么填？ 需要你在OpenAI账号下创建APIkey [详细看这里](https://beta.openai.com/docs/quickstart/add-your-api-key)
    - 项目中有一个 `ssml.xml` 配置文件，这个文件控制着语音输入/输出的语言及感情。默认配置已够用，不用修改。如果你有其他喜好可以参照这里修改。- [Voice and sound with SSML](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-synthesis-markup-voice) 你可以轻松的修改语言和感情等属性，但不建议更改DOM结构，这可能使程序出错。



4. 启动
```
& python main.py
```

5. 使用
    - 在控制台单击`Enter`键程序开始聆听(按一下，不是一直按住)，最长时间为30s，不要害羞
    - kanojyo回答完毕会等待你再次按下`Enter`键，如此重复，直到按下`Ctrl+C`

