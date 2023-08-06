# Plausible Analytics for Material

Plausible Analytics is a simple, open-source, lightweight and privacy-friendly
web analytics alternative to Google Analytics.

This plugin implements Plausible Analytics support in Material for MkDocs.


## Quick start

1. Install the plugin:

    ```sh
    pip install material-plausible-plugin
    ```


2. Add the following lines to `mkdocs.yml`:

    ```yaml
    plugins:
      - material-plausible

    extra:
      analytics:
        provider: plausible
        domain: example.com

        #: If using custom domain proxy or self-hosting Plausible,
        #: uncomment and specify script path here:
        # src: "https://plausible.example.com/js/plausible.js"

        feedback:
          title: Was this page helpful?
          ratings:
            - icon: material/emoticon-happy-outline
              name: This page was helpful
              data: good
              note: >-
                Thanks for your feedback!

            - icon: material/emoticon-sad-outline
              name: This page could be improved
              data: bad
              note: >-
                Thanks for your feedback! Help us improve this page by
                using our <a href="..." target="_blank" rel="noopener">feedback form</a>.
    ```

2. In your Plausible account, go to your website's settings and visit the **Goals** section. For each rating defined, click on the **+ Add goal** button, select **Custom event** as the goal trigger and enter `Feedback: {rating data value}`.

    For example, if you have two ratings – `good` and `bad`, add `Feedback: good` and `Feedback: bad` goals.

Ratings will be shown in the **Goal Conversions** section at the very bottom of the page, as soon as any are available:

<img width="449" alt="image" src="https://user-images.githubusercontent.com/1298948/211634195-b0131d54-cd5f-49d6-9a3d-85bdb4c493fc.png">

You can click on a specific “goal” to filter your dashboard by it. For example, if you filter by the `Feedback: bad` goal, you can see which pages need the most attention in the **Top Pages** section.


## License

`material-plausible-plugin` is distributed under the terms of the [ISC license](https://spdx.org/licenses/ISC.html).
