# Output Delivery

## Finalization order

1. select the highest-scoring approved candidate;
2. complete only approved final integration and upscale;
3. add exact text outside the generative pass;
4. add the approved Finuslugi logo outside the generative pass;
5. export the required format and dimensions;
6. inspect the exported file again;
7. show the final image in the user-facing response.

## Logo rules

From this reference directory:

- white or light background: `../../../assets/finuslugi-base.png`;
- red or dark background: `../../../assets/finuslugi-inverted.png`.

Do not redraw, restyle, distort, or generate the logo.

## Output manifest

Record:

- asset ID and version;
- Scene Specification version;
- style pack ID and version;
- transformation mode;
- source reference IDs and roles;
- final dimensions and format;
- QA score;
- critical-defect result;
- final candidate ID;
- generation or edit tool used;
- delivery confirmation.

## User-facing delivery gate

Before completing the response, verify:

- the generation or edit succeeded;
- the final candidate was selected;
- visual QA passed;
- the final image is attached or rendered in the chat;
- the response is not empty.

A tool success message without a visible final image is not delivery.
