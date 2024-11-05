export default function FAQ() {
    const faqs = [
      {
        question: "How do I submit a new request?",
        answer: "You can submit a new request by filling out the request form with a title, description, and selecting your team."
      },
      {
        question: "How do I add a new team member?",
        answer: "To add a new team member, use the contact form to enter their details including name, email, phone, and office location."
      },
      // Add more FAQs as needed
    ]
  
    return (
      <div className="space-y-6">
        <h2 className="text-2xl font-bold">Frequently Asked Questions</h2>
        <div className="space-y-4">
          {faqs.map((faq, index) => (
            <div key={index} className="border rounded-lg p-4">
              <h3 className="font-semibold text-lg">{faq.question}</h3>
              <p className="mt-2 text-gray-600">{faq.answer}</p>
            </div>
          ))}
        </div>
      </div>
    )
  }