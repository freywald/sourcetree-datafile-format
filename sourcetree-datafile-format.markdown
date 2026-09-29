# Bibliography Sources

## Core Concept

Instead of just storing URLs, we treat every entry as a **source** that can be cited. The goal is to have enough structured metadata so you can later generate proper citations (APA, MLA, Chicago, etc.) or query your sources intelligently.

## Tier 1: Universal Fields

These fields should be considered for **almost every entry**:

| Field              | Description                                      | Example                              | Recommended |
|--------------------|--------------------------------------------------|--------------------------------------|-------------|
| `type`             | Type of source                                   | `url`, `book`, `video`, `local`, `paper` | **Strongly recommended** |
| `title`            | Main title of the source                         | `The Wollemi Pine`                   | Yes |
| `author`           | Creator(s)                                       | `Wollemia nobilis` or `John Smith`   | Yes |
| `date`             | Publication / creation year or date              | `1994` or `2023-05-12`               | Yes |
| `note`             | Free-form notes or context                       | `Used in chapter 3`                  | Yes |
| `tags`             | Comma-separated tags                             | `botany, endangered, australia`      | Recommended |
| `local`         | File on your computer                | `local_path`, `format` |

### Proposed Standard `type` Values

| `type`      | Meaning                                            | Typical Fields Used                   |
|-------------|----------------------------------------------------|---------------------------------------|
| `url`       | General web page / resource                        | `url`, `archive_url`                  |
| `book`      | Physical or digital book                           | `title`, `author`, `isbn`, `page`     |
| `video`     | Online video (YouTube, etc.)                       | `url`, `timestamp`, `platform`        |
| `archive`   | Archived web content                               | `archive_url`, `original_url`         |
| `audio`     | Podcast or audio recording                         | `url`, `timestamp`                    |
| `image`     | Photograph or diagram                              | `url` or `local_path`                 |
| `paper`     | Academic paper / article                           | `doi`, `url`, `page`                  |
| `notebook`  | Bound or stapled notes, exercise books (Notizbuch) | `title`, `author`, `date` |
| `report`    | Formal or structured reports (Bericht)             | `title`, `author`, `date`, `url` |
| `journal`   | Reflective or daily personal writing (Tagebuch)    | `title`, `author`, `date`             |
| `log`       | Chronological factual records (Logbuch)            | `title`, `date`           |
| `booklet`   | Thin bound collection of pages (Heft)              | `title`, `date`           |

## Tier 2: Access & Location Fields

These define *where* the source lives:

| Field                | Description                              | Applies To                  | Example |
|----------------------|------------------------------------------|-----------------------------|--------|
| `url`                | Primary URL                              | Web sources                 | `https://...` |
| `archive_url`        | Web Archive / mirror link                | Web sources                 | `https://web.archive.org/...` |
| `alternate_url`      | Alternative working link                 | Web sources                 | - |
| `local_path`         | Path on your filesystem                  | Local files                 | `/media/books/wollemi.pdf` |
| `doi`                | Digital Object Identifier                | Academic papers             | `10.1234/abc` |
| `isbn`               | Book identifier                          | Books                       | `978-3-16-148410-0` |

## Tier 3: Citation & Reference Fields

These are especially useful when you're referencing a **specific part** of a source:

| Field               | Description                           | Applies To             | Example                                          |
|---------------------|---------------------------------------|------------------------|--------------------------------------------------|
| `page`              | Page number(s) of the quote/reference | Books, PDFs            | `p. 47` or `pp. 45-48`                           |
| `timestamp`         | Timestamp in video/audio              | Videos, audio          | `12:34` or `00:45:12`                            |
| `chapter`           | Chapter or section                    | Books, long documents  | `Chapter 4`                                      |
| `quote`             | The actual text you're referencing    | Any                    | `"...exact quote..."`                            |
| `accessed`          | Date you last accessed the source     | Web sources            | `2026-07-10`                                     |
| `references_parent` | Parent entry that is referenced       | Any            | id slugs like `QUMRAN-IN-LIGHT-OF-RAMAT-HANADIV` |

## Tier 4: Type-Specific Fields (Optional but useful)

| Field              | Description                        | Best For          | Example |
|--------------------|------------------------------------|-------------------|--------|
| `platform`         | Platform name                      | Videos            | `youtube`, `vimeo` |
| `video_id`         | Platform-specific ID               | YouTube/Vimeo     | `dQw4w9wgccc` |
| `publisher`        | Publishing company                 | Books             | `CSIRO Publishing` |
| `edition`          | Edition of the book                | Books             | `2nd edition` |
| `format`           | File format                        | Local media       | `pdf`, `mp4`, `epub` |
| `duration`         | Length of video/audio              | Videos            | `14:32` |

