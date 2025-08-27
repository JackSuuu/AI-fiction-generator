# DeepSeek AI 自动写作脚本

基于 DeepSeek API 的智能小说生成工具，能够根据自定义提示词和参考文本自动生成高质量的中文都市言情小说。

## 功能特点

- 🤖 **智能生成**：使用 DeepSeek-V3 模型生成创意小说内容
- 📖 **完整故事**：自动生成约1万字的完整短篇小说
- 🎯 **个性化**：根据用户输入的提示词定制故事类型和风格
- 📝 **纯文本输出**：去除所有 Markdown 格式，输出纯小说正文
- 📄 **Word 文档**：自动生成格式化的 Word 文档，包含合适的字体设置
- 🏷️ **智能标题**：根据故事大纲自动生成吸引人的小说标题
- 🔄 **重试机制**：具备网络重试和错误处理机制

## 环境要求

- Python 3.7+
- DeepSeek API 密钥

## 安装步骤

1. **克隆或下载项目**
   ```bash
   cd AI-auto-writer-script
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # 或
   .venv\Scripts\activate     # Windows
   ```

3. **安装依赖包**
   ```bash
   pip install requests python-docx python-dotenv
   ```

4. **配置 API 密钥**
   
   复制 `.env.example` 文件为 `.env`：
   ```bash
   cp .env.example .env
   ```
   
   编辑 `.env` 文件，填入您的 DeepSeek API 密钥：
   ```
   DEEPSEEK_API_KEY=your_api_key_here
   DEEPSEEK_BASE_URL=https://api.deepseek.com/v1/chat/completions
   ```

## 文件结构

```
AI-auto-writer-script/
├── auto_writer.py      # 主程序脚本
├── prompt.txt          # 系统提示词文件
├── example.txt         # 参考文本样例
├── .env               # 环境变量配置文件
├── .env.example       # 环境变量配置模板
├── README.md          # 项目说明文档
└── requirements.txt   # Python 依赖包列表
```

## 使用方法

1. **准备提示词文件**
   
   确保 `prompt.txt` 文件包含您想要的小说创作指导，例如：
   - 角色设定要求
   - 故事风格偏好
   - 情节发展指导
   - 语言风格要求

2. **准备参考文本**
   
   在 `example.txt` 中放入您希望模仿的小说文本片段，脚本会学习其写作风格。

3. **运行脚本**
   ```bash
   python auto_writer.py
   ```

4. **输入创作要求**
   
   程序启动后会提示您输入小说类型和要求，例如：
   ```
   请输入您想要生成的小说类型和要求（直接回车使用默认设置）：
   生成一部校园青春小说，主角是大学生，包含友情和成长元素
   ```

5. **等待生成完成**
   
   脚本会依次：
   - 生成小说大纲
   - 创建小说标题
   - 逐章生成内容
   - 保存为 Word 文档

## 输出格式

生成的 Word 文档具有以下格式特点：

- **标题**：3号字体（16pt），居中，加粗
- **正文**：5号字体（10.5pt），左对齐
- **时间信息**：小五号字体（9pt），右对齐
- **纯文本**：无章节标题，无分隔符，连续的故事正文

## 配置选项

### API 设置

在 `.env` 文件中可以配置：

```
# DeepSeek API 密钥（必填）
DEEPSEEK_API_KEY=your_api_key_here

# API 基础URL（可选，默认为官方地址）
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1/chat/completions
```

### 生成参数

可以在脚本中调整的参数：

- `total_chapters`: 章节数量（默认3章）
- `target_words`: 目标字数（默认约16000字）
- `max_tokens`: 单次API调用最大token数
- `temperature`: 创作随机性（0-1，默认0.7）

## 故障排除

### 常见问题

1. **API 密钥错误**
   ```
   错误：请在.env文件中设置DEEPSEEK_API_KEY环境变量
   ```
   **解决方案**：检查 `.env` 文件是否存在且包含正确的 API 密钥

2. **网络连接超时**
   ```
   请求超时: HTTPSConnectionPool(host='api.deepseek.com', port=443): Read timed out.
   ```
   **解决方案**：脚本会自动重试，请耐心等待或检查网络连接

3. **文件未找到**
   ```
   错误：找不到文件 prompt.txt
   ```
   **解决方案**：确保 `prompt.txt` 和 `example.txt` 文件存在于脚本同目录下

### 性能优化

- 如果生成速度较慢，可以减少 `target_words` 参数
- 网络不稳定时，脚本会自动重试，建议保持网络连接稳定
- 大型提示词可能影响生成质量，建议保持提示词简洁明确

## API 限制

- DeepSeek API 有调用频率限制，请合理使用
- 单次生成约消耗 15000-20000 tokens
- 建议在网络状况良好时使用以获得最佳体验

## 技术特性

- **重试机制**：网络异常时自动重试，最多5次
- **错误处理**：完善的异常捕获和错误提示
- **格式清理**：自动移除 Markdown 格式符号
- **文件安全**：自动处理文件名中的特殊字符

## 许可协议

本项目采用 MIT 许可协议，详见 LICENSE 文件。

## 更新日志

### v1.0.0
- 基础小说生成功能
- DeepSeek API 集成
- Word 文档输出
- 环境变量配置
- 错误处理和重试机制

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 联系方式

如有问题或建议，请通过 GitHub Issues 联系。
