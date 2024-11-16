import "@copilotkit/react-ui/styles.css";
import { CopilotSidebar } from "@copilotkit/react-ui";

function YourMainContent() {
  return (
    <div>
      {/* Your main application content */}
    </div>
  );
}

export function Copilot_App() {
  return (
    <CopilotSidebar
      defaultOpen={true}
      instructions={"You are assisting the user as best as you can. Answer in the best way possible given the data you have."}
      labels={{
        title: "Sidebar Assistant",
        initial: "How can I help you today?",
      }}
    >
      <YourMainContent />
    </CopilotSidebar>
  );
}

export default Copilot_App;


