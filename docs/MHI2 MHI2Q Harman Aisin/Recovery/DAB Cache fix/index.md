# DAB Cache fix

# What?

After some years of operation, MHI2 units with DAB (even unpatched!) can become very slow, or more seriously, stuck in in a boot loop. No reaction to button inputs, no audio output, not reachable via OBD2. Reboots every 60 seconds.

Read: Same behaviour as the ExceptionList bug, but other cause.

# Cause

The `/mnt/efs-persist` partition is running out of space, due to cache files created especially by the DAB module.


# Solution

Note: If you are stuck in the 60sec bootloop, you have to be very quick now…


1. Connect to RCC via [Telnet](/MHI2 MHI2Q Harman Aisin/Shell access via telnet and UART/Telnet/Telnet client- Putty/) (D-Link adapter) or [TTL cable](/MHI2 MHI2Q Harman Aisin/Shell access via telnet and UART/Connecting TTL adapter to UART on quadlock/), login with the password for your SW version (See [Password_List_V4.0.pdf](https://github.com/Mr-MIBonk/M.I.B._More-Incredible-Bash/blob/main/Password_List_V4.0.pdf) in M.I.B. GitHub)
2. (optional) Check free space of `/mnt/efs-persist` with `df` command. Expected to be below <5%
3. Mount persistence partition as writeable:

   `mount -uw /net/rcc/mnt/efs-persist/`
4. Delete cache files:

   `rm -R /HBpersistence/irc/*`

   `rm -R /HBpersistence/persistence/*`

   `rm -R /net/mmx/mnt/ols/rcc/epg/*`

   `rm /HBpersistence/core/*`
5. Reboot (or wait for boot loop happening)
6. Profit! The unit should now be fully operational again.


# References

<https://www.digital-eliteboard.com/threads/kostenloses-dabfix-fuer-mhi2-modelle.541645/>


\