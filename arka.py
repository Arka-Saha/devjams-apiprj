API = "AIzaSyAE2KG-hS58Xbgeu_DZ9jXGUIwnadnfZ_M"
from google import genai

client = genai.Client(api_key=API)

prompt = """
Generate detailed documentation in Markdown format for a tool called "APIForge - API Tester Tool". 
Include the following sections:
1. **Title & Description**: A short description of the tool (one paragraph). 
2. **Features**: List all core software features, hardware features, and advanced features in bullet points with short explanations. Include examples where relevant.
3. **Getting Started**: Instructions on installing dependencies, running the CLI, and starting the mock server.
4. **Usage Guide**: 
   - How to generate schemas from fields & datatypes.
   - How to run tests (GET, POST, PUT, DELETE).
   - How to measure latency & error rates.
   - How to integrate with CI/CD (GitHub Actions example).
   - How to connect to hardware dashboard (LEDs / Raspberry Pi).
5. **Test Case Generation**: Explain automatic test case generation from OpenAPI spec, including sample code snippets.
6. **Mock Server**: How to create and run a dynamic mock server from the schema.
7. **CI/CD Integration**: Explain workflow with test automation, latency checks, and deployment gating.
8. **Hardware Monitoring**: Explain LEDs or display integration, status indicators, and alerts.
9. **Advanced Features**: Load testing, network simulation, environment comparison, historical metrics, customizable thresholds.
10. **Screenshots / Code Snippets**: Include example Python snippets for each major feature.
11. **License / Contribution / Contact**: Optional placeholder sections for open-source usage.

Make the documentation **well-structured**, use **Markdown headings, subheadings, bullet points, and code blocks**, and ensure it is **clear and professional**, suitable for a GitHub README or hackathon submission.
"""


response = client.models.generate_content(
    model="gemini-2.5-pro", contents=prompt, 
)
print(response.text)