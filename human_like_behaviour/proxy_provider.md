### কত ধরনের প্রোক্সি আছে

- Residential proxies (বাসিন্দা IP) — বাড়ির ISP-এর থিকে আসা IP; ব্লক হওয়া কঠিন, কিন্তু দামী।
- Datacenter proxies — দ্রুত ও সস্তা কিন্তু বেশ কয়েকবার ব্লক হওয়া সম্ভব (ডেটা-সেন্টার আইপি)।
- ISP / Static Residential — Datacenter-র speed কিন্তু নামে-তে residential সুবিধা (কিছু প্রোভাইডার দেয়)।
- Mobile proxies — মোবাইল নেটওয়ার্ক IP (খুব ভালো যদি মোবাইল-লাইক ট্র্যাফিক দরকার)।

### রেপুটেড প্রোক্সি প্রোভাইডার

- Bright Data (Luminati) — বিশাল residential pool; enterprise features ও KYC প্রক্রিয়া আছে।
- Oxylabs — premium residential & ISP proxies, pay-as-you-go options।
- Decodo (ex-Smartproxy) — value / user-friendly; large IP pool।
- IPRoyal, SOAX, NetNut, PacketStream, Webshare, Shifter — প্রত্যেকটির নিজস্ব বৈশিষ্ট্য ও price-model আছে; তুলনা করে নেও।

### কোনটা বেছে নেবো — কি দেখে সিদ্ধান্ত নেবে

- Use case: বোঝো তুমি কি চাও — high anonymity scraping / geo testing / many sessions / low-latency automation।
- Coverage: কোন দেশ/শহর লাগে — provider pool কভার করে কিনা।
- Rotation & session control: rotating pool দরকার নাকি sticky/static IP দরকার।
- Protocols supported: HTTP(S) vs SOCKS5 — Playwright/your tool কোনটা সাপোর্ট করে দেখো।
- Pricing model: GB-based vs concurrent IPs vs subscription; পরিকল্পনা এবং বাজেট মিলাও (BrightData / Oxylabs এ GB-price দেখা যাবে)।
- Legal / Ethical sourcing: provider কীভাবে IP source করে — transparency চাইলে প্রশ্ন করো (Bright Data মতোগুলো sourcing নীতি প্রকাশ করে)।
