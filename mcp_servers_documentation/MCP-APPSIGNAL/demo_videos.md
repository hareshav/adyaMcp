# AppSignal MCP Server - Demo Videos

## Overview

This document outlines the demo videos that showcase the AppSignal MCP server capabilities. These videos demonstrate how AI assistants can interact with AppSignal monitoring data through the MCP protocol.

## Demo Video Scripts

### Demo 1: Basic Error Monitoring Setup

**Duration:** 3-5 minutes

**Objective:** Show how to set up and use the AppSignal MCP server for basic error monitoring.

**Script:**
1. **Introduction (30 seconds)**
   - "Welcome to the AppSignal MCP server demo"
   - "Today we'll show how AI assistants can monitor application errors using AppSignal"

2. **Setup (1 minute)**
   - Show the project structure
   - Demonstrate environment variable configuration
   - Explain credential requirements

3. **Basic Error Search (2 minutes)**
   - Use `search_appsignal_errors` tool
   - Show searching across organization
   - Demonstrate namespace filtering
   - Display error results with stack traces

4. **Error Analysis (1 minute)**
   - Get specific incident details
   - Show error patterns and trends
   - Demonstrate pagination

**Key Points to Highlight:**
- Easy setup process
- Real-time error data access
- Comprehensive error information
- Organization-wide search capabilities

### Demo 2: Advanced Error Analysis

**Duration:** 4-6 minutes

**Objective:** Demonstrate advanced error analysis and debugging capabilities.

**Script:**
1. **Introduction (30 seconds)**
   - "In this demo, we'll explore advanced error analysis features"
   - "We'll show how to debug specific incidents and analyze patterns"

2. **Incident Investigation (2 minutes)**
   - Use `get_appsignal_incident_details` tool
   - Show detailed stack traces
   - Demonstrate time-based filtering
   - Display performance metrics for performance incidents

3. **Error Pattern Analysis (2 minutes)**
   - Use `get_appsignal_all_errors` tool
   - Show error frequency analysis
   - Demonstrate severity filtering
   - Display error trends over time

4. **Real-world Debugging Scenario (1 minute)**
   - Simulate a production error investigation
   - Show how to trace error origins
   - Demonstrate incident correlation

**Key Points to Highlight:**
- Detailed debugging information
- Performance correlation
- Historical trend analysis
- Production-ready monitoring

### Demo 3: Performance Monitoring

**Duration:** 3-4 minutes

**Objective:** Showcase performance monitoring and incident management.

**Script:**
1. **Introduction (30 seconds)**
   - "Let's explore performance monitoring capabilities"
   - "We'll show how to track application performance and identify bottlenecks"

2. **Performance Incident Overview (2 minutes)**
   - Use `get_appsignal_all_incidents` tool
   - Show performance incident listing
   - Demonstrate state filtering
   - Display performance metrics

3. **Performance Analysis (1 minute)**
   - Analyze slow endpoints
   - Show performance thresholds
   - Demonstrate incident progression tracking

4. **Performance Optimization Insights (30 seconds)**
   - Show how data can inform optimization decisions
   - Demonstrate trend analysis

**Key Points to Highlight:**
- Performance bottleneck identification
- Threshold monitoring
- Incident state tracking
- Optimization insights

### Demo 4: Integration with AI Assistant

**Duration:** 5-7 minutes

**Objective:** Demonstrate how the MCP server integrates with AI assistants for automated monitoring.

**Script:**
1. **Introduction (30 seconds)**
   - "Now let's see how this integrates with AI assistants"
   - "We'll show automated monitoring and alerting workflows"

2. **Automated Error Monitoring (2 minutes)**
   - Show AI assistant checking for new errors
   - Demonstrate automated error categorization
   - Show severity-based alerting

3. **Intelligent Error Analysis (2 minutes)**
   - AI assistant analyzing error patterns
   - Suggesting potential root causes
   - Providing debugging recommendations

4. **Performance Monitoring Automation (1 minute)**
   - Automated performance checks
   - Threshold violation detection
   - Performance optimization suggestions

5. **Real-time Dashboard Updates (30 seconds)**
   - Show how AI can provide real-time status updates
   - Demonstrate proactive monitoring

**Key Points to Highlight:**
- Automated monitoring workflows
- Intelligent error analysis
- Proactive alerting
- AI-powered insights

## Technical Requirements for Recording

### Environment Setup
- Clean development environment
- AppSignal test account with sample data
- MCP server properly configured
- AI assistant (Claude, GPT, etc.) with MCP integration

### Sample Data Requirements
- Multiple applications with various error types
- Performance incidents with different severity levels
- Historical data for trend analysis
- Realistic error scenarios

### Recording Tools
- Screen recording software (OBS, Camtasia, etc.)
- Audio recording capability
- Video editing software for post-production

## Demo Scenarios

### Scenario 1: E-commerce Application Monitoring
- Monitor payment processing errors
- Track checkout performance
- Analyze user experience issues

### Scenario 2: API Service Monitoring
- Monitor API endpoint errors
- Track response time degradation
- Analyze service dependencies

### Scenario 3: Microservices Architecture
- Monitor inter-service communication
- Track distributed tracing
- Analyze service mesh performance

## Best Practices for Demo Videos

### Content Guidelines
1. **Keep it Realistic**: Use real-world scenarios and data
2. **Show Value**: Demonstrate clear benefits and use cases
3. **Progressive Complexity**: Start simple, build to advanced features
4. **Error Handling**: Show how the system handles edge cases

### Presentation Guidelines
1. **Clear Narration**: Explain what's happening at each step
2. **Visual Clarity**: Use clear fonts and good contrast
3. **Pacing**: Don't rush through complex operations
4. **Callouts**: Highlight important features and results

### Technical Guidelines
1. **Stable Environment**: Ensure all tools work reliably
2. **Backup Plans**: Have alternative scenarios ready
3. **Quality Audio**: Use good microphone and quiet environment
4. **Professional Editing**: Clean up mistakes and add captions

## Success Metrics

### Engagement Metrics
- Video completion rates
- Viewer retention at key points
- Comments and questions
- Social media shares

### Technical Metrics
- Setup success rate
- Tool usage adoption
- Error resolution time
- Performance improvement tracking

## Future Demo Ideas

### Advanced Features
- Custom alert creation
- Multi-application dashboard
- Historical trend analysis
- Integration with external tools

### Use Case Specific
- DevOps workflow integration
- CI/CD pipeline monitoring
- Security incident monitoring
- Compliance reporting automation 