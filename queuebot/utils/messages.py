# Strings taken from https://github.com/b1naryth1ef.

__all__ = (
    'BOT_BROKEN_MSG',
    'COUNCIL_QUEUE_MSG_NOT_FOUND',
    'BAD_SUGGESTION_MSG',
    'SUGGESTION_RECEIVED',
    'SUGGESTION_APPROVED',
    'SUGGESTION_DENIED',
    'SUGGESTION_TOO_LARGE',
    'UPLOADED_EMOJI_NOT_FOUND',
    'SUBMITTER_NOT_FOUND'
)

COUNCIL_QUEUE_MSG_NOT_FOUND = (
    "\N{WARNING SIGN} Couldn't delete the associated council queue message "
    "(ID: `{suggestion[council_message_id]}`) for {suggestion[idx]}: {error}"
)

UPLOADED_EMOJI_NOT_FOUND = (
    "\N{WARNING SIGN} Cannot {action}, the uploaded emoji associated with this suggestion wasn't found. "
    "(Suggestion ID: {suggestion[idx]})"
)

SUBMITTER_NOT_FOUND = (
    "\N{WARNING SIGN} Warning during {action}: the user associated with this suggestion wasn't found. "
    "Proceeding anyways. (Suggestion ID: {suggestion[idx]}, user ID: {suggestion[user_id]})"
)

BAD_SUGGESTION_MSG = (
    'Heya! Looks like you tried to suggest '
    'an emoji to the Cowboy Emoji Server Unfortunately it looks like '
    'you didn\'t send your message in the right format, so I wasn\'t able '
    'to understand it. To suggest an emoji, you must post the emoji name, '
    'like so: `:my_emoji_name:` and upload the emoji as an attachment. Feel '
    'free to try again.'
)

SUGGESTION_TOO_LARGE = (
    'Hey there! Looks like you tried to submit an emoji, but it was '
    'too large to accept (it must be under 256kb).\nIf it\'s static, '
    'try making it smaller (but at least 128x128).\nIf it\'s animated, '
    'try reducing the length of the animation or reducing the framerate.\n'
    'Once you\'ve limbo\'d under the 256kb bar, you can submit again '
    'and we\'ll be able to review it for you.'
)

SUGGESTION_RECEIVED = (
    'Thanks for your emoji submission ({suggestion}) to the '
    'Cowboy Emoji Server! It\'s been added to our internal vote queue, '
    'so expect an update soon! Your suggestion was left in the channel as a '
    'public indication, please don\'t delete it!'
)

SUGGESTION_APPROVED = (
    'Looks like your emoji suggestion {suggestion} has passed through our '
    'internal queue! Go vote for your suggestion in <#595641425115217921>!'
)

SUGGESTION_DENIED = (
    'Unfortunately, your emoji suggestion {suggestion} was denied after going '
    'through internal review. Feel free to keep suggesting more emoji, but please '
    'don\'t submit the same one unless you\'ve modified it significantly!'
)

# hope this never happens :3
BOT_BROKEN_MSG = (
    'Looks like QueueBot is currently having some technical difficulties. '
    'The Staff have been informed and this problem will be fixed.'
)
