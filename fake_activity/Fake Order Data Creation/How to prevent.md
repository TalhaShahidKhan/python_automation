ডুপ্লিকেট ডেটা / ডুপ্লিকেট অর্ডার তৈরি হওয়া
- একই কাস্টমার একাধিকবার ক্লিক করলে বা API বারবার ট্রিগার হলে একই অর্ডার বারবার তৈরি হয়।

ভুল বা অসম্পূর্ণ ডেটা সেভ হওয়া
- নাম, মোবাইল, অ্যাড্রেস বা প্রোডাক্ট ইনফো না থাকা—ফলাফল, ভুল অর্ডার প্রসেসিং।

লোড বেশি হলে অর্ডার ক্রিয়েশন স্লো বা ব্যর্থ হওয়া
- হঠাৎ ট্র্যাফিক বেড়ে গেলে সার্ভার স্লো হয়ে যায়—Order Pending বা Failed হয়।

স্টক সিঙ্ক না হওয়ার কারণে ভুল অর্ডার তৈরি
- ওয়েবসাইটে স্টক আছে দেখাচ্ছে, কিন্তু আসলে নেই—Customer Order place করে ফেলে।

ফেক অর্ডার বা Bot-generated Order
- বট বা স্প্যামার ফর্ম সাবমিট করে ভুল/ফেক অর্ডার তৈরি করে → ব্যবসায়িক লস বাড়ে।


========================================================================

Duplicate Prevention Logic ব্যবহার করুন - Order creation-এ
- unique order token
- throttling

Strong Validation & Required Field Check
- Name, phone, email, address, product ID → সবকিছু validate করুন।
কিছু Missing থাকলে অর্ডার তৈরি না হওয়াই ভালো।

Queue বা Background Job ব্যবহার করুন
- হায় ট্র্যাফিক সিচুয়েশনে Order Creation → Queue / Worker (BullMQ, Redis Queue, Laravel Queue)
ব্যবহার করলে কখনো ফেইল হয় না।

CAPTCHA / Rate Limit ব্যবহার করুন ফেক অর্ডার আটকাতে:

- reCAPTCHA
- hCaptcha
- IP Rate Limit
- Bot detection
