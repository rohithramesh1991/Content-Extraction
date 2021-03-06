﻿#User defined function

%%time

def content_extractor(content, start=None, end=None):

  try:

    if start and content and end:

      builder="{}(.*)(?={})".format(start,end)

      pattern=re.compile(builder)

      return pattern.search(content).group(0)

    else:

      return content

  except Exception as e:

    return content

    

ser1=df.apply(lambda x: content_extractor(x,"start_text","end_text"))