from openai import OpenAI
import config
with open('symbol.txt', 'r') as file:
    symbol = file.read().strip()
print(symbol)
client = OpenAI(
    base_url='http://localhost:11434/v1/',

    # required but ignored
    api_key='ollama',
)
prompt = """Extract the relevant company name, stock symbol, and category from the given news article. Return only one matched company, along with its corresponding symbol and category, in a JSON format. If any value cannot be determined, use `null`.

# Steps

1. Parse and extract relevant company names and contextual stock-related information from the input article.
2. Match a company to its corresponding stock symbol, using a database or other provided source.
3. Construct a JSON object for the matched company with the `Symbol`, `CompanyName`, and `CategoryName`.

# Output Format

The output should be a single JSON object with the following structure:

```json
{
  "Symbol": "[Stock Symbol]",
  "CompanyName": "[Company Name]",
  "CategoryName": "[Category Name]"
}
```

If no match is found, replace the corresponding fields with `null`.

# Examples

**Example 1**

**Input Article:**
"CTCP Quảng cáo trực tuyến 24H, Công ty cổ phần 32 và Công ty Cổ phần Tập đoàn Tiên Sơn Thanh Hóa đang được chú ý bởi giá cổ phiếu tăng mạnh."

**Output:**
```json
{
  "Symbol": "24H",
  "CompanyName": "CTCP Quảng cáo trực tuyến 24H",
  "CategoryName": "Công nghệ"
}
```

**Example 2**

**Input Article:**
"Tập đoàn Đầu tư Việt Nam với giá cổ phiếu VNI tăng mạnh trong quý I năm nay và Công ty Điện lực Hà Nội cũng nhận được sự quan tâm của các nhà đầu tư."

**Output:**
```json
{
  "Symbol": "VNI",
  "CompanyName": "Tập đoàn Đầu tư Việt Nam",
  "CategoryName": "Đầu tư tài chính"
}
```

**Example 3**

**Input Article:**
"Bản tin gần đây nhắc đến Công ty X nhưng không cung cấp thêm thông tin chi tiết khác về cổ phiếu."

**Output:**
```json
{
  "Symbol": null,
  "CompanyName": "Công ty X",
  "CategoryName": null
}
```

**Example 4**

**Input Article:**
"Không có thông tin rõ ràng về các công ty hoặc cổ phiếu trong bài viết này."

**Output:**
```json
{
  "Symbol": null,
  "CompanyName": null,
  "CategoryName": null
}
```

# Notes

- Ensure that the extracted company names match the names found in the article.
- Handle the variety of formatting in an article to extract key entities precisely.
- The output must include only one company, even if multiple companies are mentioned in the article.
- If no match is found, output with fields set to `null`.
- Provide varied output reflecting different scenarios: lack of data, ambiguous information, or extraction failures. This will help ensure the system's adaptability to real-world contexts.


"""
def summary_text(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",

                "content": prompt
            },
            {
                'role': 'user',
                'content':  f"dựa vào thông tin Symbol, CompanyName, CategoryName của  các công ty dưới đây trả lời cho tôi: \n {symbol}"
            },
            {
                'role': 'user',
                'content': text
            }
        ],
        temperature=0,
        max_tokens = 512,
        
        #request_timeout=config.REQUEST_TIMEOUT,
        model='llama3.2',
        response_format={
            "type": "json_object"
        }
    )
    keyword = chat_completion.choices[0].message.content
    return keyword
print(summary_text(input()))