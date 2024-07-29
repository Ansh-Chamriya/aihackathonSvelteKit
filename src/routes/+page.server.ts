/** @type {import('./$types').Actions} */
export const actions = {
  default: async ({ request }: { request: any }) => {
    const formData = await request.formData();
    const prompt = formData.get("prompt");
    console.log("prompt:", prompt);

    // TODO: Fetch response here
  },
};
