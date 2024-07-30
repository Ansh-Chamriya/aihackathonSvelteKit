/** @type {import('./$types').Actions} */
export const actions = {
  default: async ({ request }: { request: any }) => {
    const formData = await request.formData();
    const prompt = formData.get("prompt");
    console.log("prompt:", prompt);

    // TODO: Fetch response here
    const data = await fetch(
      "https://bxdwqjsk-8000.inc1.devtunnels.ms/predict",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "allow-acess-control-origin": "*",
        },

        body: JSON.stringify({ description: prompt }),
      }
    );
    const response = await data.json();
    console.log("response:", response);
  },
};
