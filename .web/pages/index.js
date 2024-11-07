/** @jsxImportSource @emotion/react */


import { ErrorBoundary } from "react-error-boundary"
import { Fragment, useCallback, useContext, useEffect, useState } from "react"
import { ColorModeContext, EventLoopContext } from "$/utils/context"
import { Event, getBackendURL, isTrue, refs } from "$/utils/state"
import { WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { toast, Toaster } from "sonner"
import env from "$/env.json"
import { Box as RadixThemesBox, Button as RadixThemesButton, Flex as RadixThemesFlex, Link as RadixThemesLink, Text as RadixThemesText } from "@radix-ui/themes"
import NextLink from "next/link"
import NextHead from "next/head"



                function Fallback({ error, resetErrorBoundary }) {
                    return (
                        <div>
  <p>
  {"Ooops...Unknown Reflex error has occured:"}
</p>
  <p css={({ ["color"] : "red" })}>
  {error.message}
</p>
  <p>
  {"Please contact the support."}
</p>
</div>
                    );
                }
            

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Fragment_ecc7fc8159e7de57fc1e48e5f03b41bb () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue((connectErrors.length > 0)) ? (
  <Fragment>
  <LucideWifiOffIcon css={({ ["color"] : "crimson", ["zIndex"] : 9999, ["position"] : "fixed", ["bottom"] : "33px", ["right"] : "33px", ["animation"] : (pulse+" 1s infinite") })} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Toaster_9d6e054b03c6e5d1bea1c0a5576b4e6d () {
  const { resolvedColorMode } = useContext(ColorModeContext)


  refs['__toast'] = toast
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const toast_props = ({ ["description"] : ("Check if server is reachable at "+getBackendURL(env.EVENT).href), ["closeButton"] : true, ["duration"] : 120000, ["id"] : "websocket-error" });
  const [userDismissed, setUserDismissed] = useState(false);
  (useEffect(
() => {
    if ((connectErrors.length >= 2)) {
        if (!userDismissed) {
            toast.error(
                `Cannot connect to server: ${((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : '')}.`,
                {...toast_props, onDismiss: () => setUserDismissed(true)},
            )
        }
    } else {
        toast.dismiss("websocket-error");
        setUserDismissed(false);  // after reconnection reset dismissed state
    }
}
, [connectErrors]))

  return (
    <Toaster closeButton={false} expand={true} position={"bottom-right"} richColors={true} theme={resolvedColorMode}/>
  )
}

export function Div_64093a13086094dda35345330da0660b () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <div css={({ ["position"] : "fixed", ["width"] : "100vw", ["height"] : "0" })} title={("Connection Error: "+((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''))}>
  <Fragment_ecc7fc8159e7de57fc1e48e5f03b41bb/>
</div>
  )
}

export function Errorboundary_d9b813fc0ee383a26145dbb23f858f85 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_error_81de1ebf543e512ddcedab4ae1d07cc1 = useCallback(((_error, _info) => ((addEvents([(Event("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception", ({ ["stack"] : _error["stack"], ["component_stack"] : _info["componentStack"] }), ({  })))], [_error, _info], ({  }))))), [addEvents, Event])


  return (
    <ErrorBoundary FallbackComponent={Fallback} onError={on_error_81de1ebf543e512ddcedab4ae1d07cc1}>
  <Fragment>
  <Div_64093a13086094dda35345330da0660b/>
  <Toaster_9d6e054b03c6e5d1bea1c0a5576b4e6d/>
</Fragment>
  <Fragment>
  <RadixThemesBox css={({ ["width"] : "100%" })}>
  <RadixThemesFlex css={({ ["position"] : "sticky", ["top"] : "0", ["backgroundColor"] : "#f1bf98", ["justifyContent"] : "center", ["alignContent"] : "center", ["flexDirection"] : "row", ["width"] : "100%", ["zIndex"] : "100" })}>
  <RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["height"] : "5rem", ["gap"] : "9rem" })} gap={"3"}>
  <RadixThemesBox>
  <RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>
  <NextLink href={"/"} passHref={true}>
  <RadixThemesButton css={({ ["color"] : "white", ["backgroundColor"] : "#556b2f", ["&:hover"] : ({ ["opacity"] : 0.7 }) })} variant={"soft"}>
  {"Home"}
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
</RadixThemesBox>
  <RadixThemesBox>
  <RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>
  <NextLink href={"/recetasss"} passHref={true}>
  <RadixThemesButton css={({ ["color"] : "white", ["backgroundColor"] : "#556b2f", ["&:hover"] : ({ ["opacity"] : 0.7 }) })} variant={"soft"}>
  {"Recetas"}
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
</RadixThemesBox>
  <RadixThemesBox>
  <RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>
  <NextLink href={"/misrecetas"} passHref={true}>
  <RadixThemesButton css={({ ["color"] : "white", ["backgroundColor"] : "#556b2f", ["&:hover"] : ({ ["opacity"] : 0.7 }) })} variant={"soft"}>
  {"Mis Recetas"}
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesFlex css={({ ["width"] : "100%", ["backgroundColor"] : "#eee5e9", ["height"] : "100vh" })}>
  <RadixThemesFlex css={({ ["justifyContent"] : "center", ["alignContent"] : "center", ["width"] : "100%" })}>
  <RadixThemesText as={"p"} css={({ ["fontSize"] : "8rem", ["color"] : "#556b2f", ["textShadow"] : "1px 1px 1px black" })}>
  {"Comarca Code Recetas App"}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesBox>
</Fragment>
  <NextHead>
  <title>
  {"Proyecto Info | Index"}
</title>
  <meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</ErrorBoundary>
  )
}

export default function Component() {

  return (
    <Errorboundary_d9b813fc0ee383a26145dbb23f858f85/>
  )
}
