# $NetBSD$

GITHUB_PROJECT=	nox
DISTNAME=	2025.10.14
GITHUB_TAG=	refs/tags/${DISTNAME}
PKGNAME=	${PYPKGPREFIX}-${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_GITHUB:=wntrblm/}
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/wntrblm/nox/
COMMENT=	Flexible test automation for Python
LICENSE=	apache-2.0

WRKSRC=		${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}
USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-hatchling>=0:../../devel/py-hatchling
DEPENDS+=	${PYPKGPREFIX}-argcomplete>=1.9.4:../../devel/py-argcomplete
DEPENDS+=	${PYPKGPREFIX}-colorlog>=2.6.1:../../devel/py-colorlog
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=0:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-packaging>=20.9:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=3.7.4:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-virtualenv>=14:../../devel/py-virtualenv
DEPENDS+=	${PYPKGPREFIX}-jinja2>=0:../../textproc/py-jinja2
DEPENDS+=	${PYPKGPREFIX}-tox>=0:../../devel/py-tox

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
