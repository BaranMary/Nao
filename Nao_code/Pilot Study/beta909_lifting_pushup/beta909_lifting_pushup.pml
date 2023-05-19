<?xml version="1.0" encoding="UTF-8" ?>
<Package name="beta909_lifting_pushup" format_version="5">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="dolifting" src="dolifting/dolifting.dlg" />
        <Dialog name="pushup" src="pushup/pushup.dlg" />
        <Dialog name="saysetgoal" src="saysetgoal/saysetgoal.dlg" />
    </Dialogs>
    <Resources>
        <File name="Fireworks" src="Fireworks.mp3" />
        <File name="Inspiration" src="Inspiration.mp3" />
    </Resources>
    <Topics>
        <Topic name="dolifting_enu" src="dolifting/dolifting_enu.top" topicName="dolifting" language="en_US" nuance="enu" />
        <Topic name="pushup_enu" src="pushup/pushup_enu.top" topicName="pushup" language="en_US" nuance="enu" />
        <Topic name="saysetgoal_enu" src="saysetgoal/saysetgoal_enu.top" topicName="saysetgoal" language="en_US" nuance="enu" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
