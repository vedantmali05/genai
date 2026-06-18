from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated, Optional, Literal

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Summarizer(TypedDict):
    keywords: Annotated[list[str], "List of all features discussed in the input review."]
    summary: Annotated[str, "A brief summary of the input review."]
    sentiments: Annotated[Literal["positive", "neutral", "negative", "mixed"], "The overall sentiment of the review."]
    pros: Annotated[Optional[list[str]], "Pros of the product."]
    cons: Annotated[Optional[list[str]], "Cons of the product."]
    number_of_words: Annotated[int, "Total number of words in the review."]

structured_model = model.with_structured_output(Summarizer)

result = structured_model.invoke("""
Samsung Galaxy S24 Ultra Review: A Powerhouse with Minor Caveats

I have been using the new Samsung Galaxy S24 Ultra as my primary device for the past three weeks, and it has been an impressive, yet familiar, journey. The hardware feels extremely premium with its new titanium frame, which offers a much better grip and a sleek, industrial aesthetic compared to its predecessor. 

Under the hood, the Snapdragon 8 Gen 3 processor is an absolute monster. App launches are instantaneous, multitasking with split-screen is effortless, and heavy gaming runs at a consistent 120 FPS without any noticeable thermal throttling. However, the processor experience does have a slight quirk: under sustained workloads like 4K video rendering, the back glass gets noticeably warm, and I noticed a slight frame drop in the camera app UI when switching rapidly between lenses. 

The 5,000mAh battery has been stellar. On average, I get about 8 to 9 hours of screen-on time with heavy use, easily lasting a full day and a half. Charging speed is decent but at 45W, it lags behind competitor speeds.
- Phenomenal Snapdragon 8 Gen 3 performance.
- Excellent 1.5-day battery life with 8+ hours of Screen-on-Time.
- Beautiful, bright flat AMOLED display with reduced reflections.
- Titanium build feels premium and durable.
- 45W charging is slow compared to Chinese flagships.
- Minor stutter in camera app UI when switching lenses.
- Extremely expensive, starting at $1,299.
- Large footprint makes one-handed usage uncomfortable.
""")

print(result)