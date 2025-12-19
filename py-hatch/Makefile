# $NetBSD$

DISTNAME=	hatch-1.16.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=h/hatch/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/hatch/
COMMENT=	Hatch is a modern, extensible Python project manager
LICENSE=	mit

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-hatchling>=1.14.0:../../devel/py-hatchling
DEPENDS+=	${PYPKGPREFIX}-click>=8.0.3:../../devel/py-click
DEPENDS+=	${PYPKGPREFIX}-httpx>=0.22.0:../../www/py-httpx
DEPENDS+=	${PYPKGPREFIX}-hyperlink>=21.0.0:../../www/py-hyperlink
DEPENDS+=	${PYPKGPREFIX}-keyring>=23.5.0:../../security/py-keyring
DEPENDS+=	${PYPKGPREFIX}-packaging>=21.3:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-pexpect>=4.8:../../devel/py-pexpect
DEPENDS+=	${PYPKGPREFIX}-platformdirs>=2.5.0:../../misc/py-platformdirs
DEPENDS+=	${PYPKGPREFIX}-pyperclip>=1.8.2:../../x11/py-pyperclip
DEPENDS+=	${PYPKGPREFIX}-rich>=11.2.0:../../comms/py-rich
DEPENDS+=	${PYPKGPREFIX}-shellingham>=1.4.0:../../misc/py-shellingham
DEPENDS+=	${PYPKGPREFIX}-tomli_w>=1.0:../../textproc/py-tomli_w
DEPENDS+=	${PYPKGPREFIX}-tomlkit>=0.11.1:../../textproc/py-tomlkit
DEPENDS+=	${PYPKGPREFIX}-userpath>=1.7:../../pkgsrc_myownpkgs/py-userpath
DEPENDS+=	${PYPKGPREFIX}-virtualenv>=20.16.2:../../devel/py-virtualenv

post-install:
	cd ${DESTDIR}${PREFIX}/bin && ${MV} hatch hatch-${PYVERSSUFFIX}

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
