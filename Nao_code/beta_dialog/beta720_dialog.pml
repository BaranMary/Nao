<?xml version="1.0" encoding="UTF-8" ?>
<Package name="beta720_dialog" format_version="5">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="greetings" src="greetings/greetings.dlg" />
        <Dialog name="introduction" src="introduction/introduction.dlg" />
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="interest" src="interest/interest.dlg" />
    </Dialogs>
    <Resources>
        <File name="mikhael-landscape-paisaje" src="behavior_1/sounds/mikhael-landscape-paisaje.ogg" />
    </Resources>
    <Topics>
        <Topic name="greetings_enu" src="greetings/greetings_enu.top" topicName="greetings" language="en_US" nuance="enu" />
        <Topic name="introduction_enu" src="introduction/introduction_enu.top" topicName="introduction" language="en_US" nuance="enu" />
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" nuance="enu" />
        <Topic name="interest_enu" src="interest/interest_enu.top" topicName="interest" language="en_US" nuance="enu" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
